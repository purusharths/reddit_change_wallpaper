import urllib
from bs4 import BeautifulSoup
#r = re.search('[htps:/]+imgur.com/a/[a-zA-Z0-9./:]+',a).group()
#album_url = 'http://imgur.com/a/pUYz7'


def get_album_photos(album_url, param=0):
	a = urllib.urlopen(album_url)
	a = a.read()
	soup = BeautifulSoup(a, 'html.parser')
	search = str(soup.find('div', {'class':'post-images'}))
	soup = BeautifulSoup(search, 'html.parser')
	if param == 1:
		urls = get_all_photo_url(soup)
		import random
		ran = urls[random.randint(0,len(urls))]
		return ran
	tag = soup.find('div', {'class': 'post-image-container post-image-container--spacer'})
	tag.attrs['id']
	url = 'i.imgur.com/'+str(tag.attrs['id'])+'.jpg'
	return url

def get_all_photo_url(soup):
	tager = soup.find_all('div', {'class': 'post-image-container post-image-container--spacer'})
	list_of_urls = []
	for tag in tager:
		url = 'i.imgur.com/'+str(tag.attrs['id'])+'.jpg'
		list_of_urls.append(url)
	return list_of_urls

if __name__ == '__main__':
 get_album_photos('http://imgur.com/a/pUYz7', param=1)

"""
tager = soup.find_all('div', {'class': 'post-image-container post-image-container--spacer'})
list_of_urls = []
for tag in tager:
	list_of_urls.append(tag)

"""