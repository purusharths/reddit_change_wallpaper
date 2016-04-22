import urllib
from bs4 import BeautifulSoup
#r = re.search('[htps:/]+imgur.com/a/[a-zA-Z0-9./:]+',a).group()
#album_url = 'http://imgur.com/a/pUYz7'


def get_album_photos(album_url, param=0, random_fill=0):
	a = urllib.urlopen(album_url)
	a = a.read()
	soup = BeautifulSoup(a, 'html.parser')
	search = str(soup.find('div', {'class':'post-images'}))
	soup = BeautifulSoup(search, 'html.parser')
	if param == 1:
		urls = get_all_photo_url(soup)
		if random_fill == 1:
			return urls
		else:
			import random
			ran = urls[random.randint(0,len(urls))]
			return ran
	tag = soup.find('div', {'class': 'post-image-container post-image-container--spacer'})
	tag.attrs['id']
	url = 'http://i.imgur.com/'+str(tag.attrs['id'])+'.jpg'
	return url

def get_all_photo_url(soup):
	tager = soup.find_all('div', {'class': 'post-image-container post-image-container--spacer'})
	list_of_urls = []
	for tag in tager:
		url = 'http://i.imgur.com/'+str(tag.attrs['id'])+'.jpg'
		list_of_urls.append(url)
	return list_of_urls

if __name__ == '__main__':
	import sys
	import re
	album_url = sys.argv[1]
	is_album = re.findall('[htps:/]+imgur.com/a/[a-zA-Z0-9./]+', album_url)
	if not is_album:
		print "Invalid Imgur album url: {} \nMake sure to include the 'http://'\n".format(album_url)
		exit()
	print "Album URL: {}".format(album_url)
 	urls = get_album_photos(album_url, param=1, random_fill=1)
 	import random
 	for url in urls:
 		urllib.urlretrieve(url, str(random.randint(0,99999999))+".jpg")

"""

tager = soup.find_all('div', {'class': 'post-image-container post-image-container--spacer'})
list_of_urls = []
for tag in tager:
	list_of_urls.append(tag)

"""