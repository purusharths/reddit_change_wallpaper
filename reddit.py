import requests
from bs4 import BeautifulSoup
import re
import urllib
from change_background import apply_background

head = {'User-Agent': 'Mozilla/5.0'}
def calling(subreddit):
	r = requests.get("https://www.reddit.com/r/"+subreddit, headers = head)
	if r.status_code == 200:
		print r.status_code
		text = r.text
		soup = BeautifulSoup(text, "html.parser")
		
		search_string = str(soup.find('a', {'class':'title'}))
		print search_string
		#https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,}
		#[htps:/]{7,8}[a-zA-Z0-9./:.]+[a-zA-Z0-9./:.]
		photo_url = str(re.search('[htps:/]{7,8}[a-zA-Z0-9._/:.]+[a-zA-Z0-9./:.]', search_string).group())
		print search_string+"\n\n\n\n"
		if photo_url[-4:]!=".jpg":
			photo_url = photo_url+".jpg"
		print photo_url
		photo_name = re.findall(r'(>)([\w\s,().{}\[\]]+)(<?)',search_string)
		print photo_name
		photo_name = photo_name[0][1]+".jpg"
		urllib.urlretrieve(photo_url, photo_name)
		print photo_name
		a = apply_background(photo_name)
	else:
		print "Something went wrong!"
		print r.status_code

calling("Wallpapers")