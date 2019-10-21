from sys import argv
import requests
from bs4 import BeautifulSoup as scrap
import pytube

script, search = argv

#Url to search any video
base='https://www.youtube.com/results?search_query='
if (search!=None):
	#If we only want to search a concrete video or playlist
	#we will changed the search by a singular url
	print('Hola %s'%search)
	req= requests.get(base+search)
	pageSearch=req.text
	#This is all html that appears in this searchpage
	soup=scrap(pageSearch,'html.parser')
#	print(soup)
	urlVideos=soup.find_all('a',class_="yt-uix-tile-link")
#	print(urlVideos)
	listUrlVideos=[]
	for video in urlVideos:
		item='https://www.youtube.com'+video['href']
		listUrlVideos.append(item)
		print(item)
		vid=pytube.YouTube(item)
		vid.streams.first().download()
	
else:
	print('Es necesario un parametro de busqueda');


