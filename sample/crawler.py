from sys import argv
import requests
import textFile
from bs4 import BeautifulSoup as scrap
import pytube
import os

script, fileName = argv

print(fileName)
if(fileName!=None):
	file= textFile.TextFile(fileName)
	list=file.listUrls()
	os.mkdir("VideosTFG")
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
				print(isPlaylist)
				titlePlaylist=soup.find_all('h3',"playlist-title")[0].contents[1].string
				if(os.path.exists(titlePlaylist.rstrip(" "))!=True):
					os.mkdir(titlePlaylist.rstrip(" "))
				htmlVideos=soup.find_all('a',"playlist-video")
				os.chdir(titlePlaylist.rstrip(" "))
				for htmlVideo in htmlVideos:
					urlItem='https://www.youtube.com'+htmlVideo['href']
					print(urlItem)
					vid=pytube.YouTube(urlItem)
					vid.streams.first().download()
					captions=vid.captions.all()
					for cap in captions:
						print(cap)
					caption=vid.captions.get_by_language_code('es')
					if (caption==None):
						caption=vid.captions.get_by_language_code('es-ES')
					if(caption!=None):
						subtitles=open(vid.title+'.txt','w')
						subtitles.write(caption.generate_srt_captions())
						subtitles.close()
				os.chdir("..")
			else:
				vid=pytube.YouTube(item)
				vid.streams.first().download()
				caption=vid.captions.get_by_language_code('es')
				print(caption)
				if (caption!=None):	
					subtitles=open(vid.title+'.txt','w')
					subtitles.write(caption.generate_srt_captions())
					subtitles.close()
				#print(soup)
	else:
		raise Exception('The file name is wrong.')
else:
	raise Exception('The number of params is wrong.')


