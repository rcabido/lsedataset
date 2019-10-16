from sys import argv
import requests
from bs4 import BeautifulSoup as scrap

script, search = argv

#Url to search any video
base='https://www.youtube.com/results?search_query='
if (search!=None):
	print('Hola %s'%search)
	req= requests.get(base+search)
	pageSearch=req.text
	#This is all html that appears in this searchpage
	soup=scrap(pageSearch,'html.parser')
	print(soup)
else:
	print('Es necesario un parametro de busqueda');


