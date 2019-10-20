from sys import argv
import requests
from bs4 import BeautifulSoup as scrap
import pytube
from ytbObject import ytbObject
import os

script, fileName = argv

print(fileName)
list=[]
if(fileName!=None):
	f=open(fileName,'r')
	mensaje=f.readlines()
	f.close()
	for linea in mensaje:
		l=linea.rstrip('\n')
		aux=l.split(',')
		print(aux)
		objAux=ytbObject(aux[0],"True"==aux[1])
		list.append(objAux)
	for item in list:
		if (item.isPlaylist):
			req=requests.get(item.link)
			pagePlaylist=req.text
			soup=scrap(pagePlaylist,'html.parser')
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
			req=requests.get(item.link)
			pageVideo=req.text
			soup=scrap(pageVideo,'html.parser')
			vid=pytube.YouTube(item.link)
			vid.streams.first().download()
			caption=vid.captions.get_by_language_code('es')
			print(caption)
			if (caption!=None):	
				subtitles=open(vid.title+'.txt','w')
				subtitles.write(caption.generate_srt_captions())
				subtitles.close()
			#print(soup)
else:
	print('Es necesario un parametro de busqueda');


