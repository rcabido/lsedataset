import requests
import textFile
from bs4 import BeautifulSoup as scrap
import pytube
import os

class Crawler (object):
	def __init__(self,filename):
		self.fileName=filename + '.txt'

	def crawlFile(self):
		videos = []
		if(self.fileName!=None):
			file= textFile.TextFile(self.fileName)
			list=file.listUrls()
			if(len(list)>0):
				for item in list:
					req=requests.get(item)
					page=req.text
					soup=scrap(page,'html.parser')
					playlist=soup.find_all('h3',"playlist-title")
					isPlaylist=True
					if (len(playlist)<1):
						isPlaylist=False
					if (isPlaylist):
						titlePlaylist=soup.find_all('h3',"playlist-title")[0].contents[1].string
						htmlVideos=soup.find_all('a',"playlist-video")
						for htmlVideo in htmlVideos:
							videos.append('https://www.youtube.com'+htmlVideo['href'])
					else:
						videos.append(item)
				return videos
			else:
				raise Exception('The file name is wrong.')
		else:
			raise Exception('The number of params is wrong.')

	def searchVideos(self):
		base='https://www.youtube.com/results?search_query='
		if (self.fileName!=None):
			print('Searching to %s'%self.fileName)
			req= requests.get(base+self.fileName)
			pageSearch=req.text
			#This is all html that appears in this searchpage
			soup=scrap(pageSearch,'html.parser')
			urlVideos=soup.find_all('a',class_="yt-uix-tile-link")
			listUrlVideos=[]
			for video in urlVideos:
				item='https://www.youtube.com'+video['href']
				listUrlVideos.append(item)
			return listUrlVideos
		else:
			print('The number of params is wrong.');

	def downloadItem(item):
		try:
			vid=pytube.YouTube(item)
			print("Downloading " + item + "...")
			titleVideo=vid.title.replace(" ", "")
			vid.streams.filter(progressive=True, file_extension='mp4').first().download(filename=titleVideo)
			caption=vid.captions.get_by_language_code('es')
			if (caption==None):
				caption=vid.captions.get_by_language_code('es-ES')
			if (caption!=None):
				print("Saving the captions of " + vid.title)
				subtitles=open(titleVideo+'.txt','w')
				subtitles.write(caption.generate_srt_captions())
				subtitles.close()
			return os.getcwd() + "/" + titleVideo + '.mp4'
		except Exception as e:
			print("Video Unavailable.")
			return None	




