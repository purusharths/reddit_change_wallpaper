import urllib
import re

import requests
from bs4 import BeautifulSoup
from change_background import apply_background
from PIL import Image

head = {'User-Agent': 'Mozilla/5.0'}

def image_check(image):
	im=Image.open(image)
	is_image = im.size
	print "Resolution: {}".format(is_image)
	if is_image:
		return True
	else:
		return False


def calling(subreddit):
	r = requests.get("https://www.reddit.com/r/"+subreddit, headers = head)
	if r.status_code == 200:
		print r.status_code
		text = r.text
		soup = BeautifulSoup(text, "html.parser")
		
		search_string = str(soup.find('a', {'class':'title'}))
		print "Found: {}\n".format(search_string)
		#https?:\/\/(?:www\.|(?!www))[^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,}
		#[htps:/]{7,8}[a-zA-Z0-9./:.]+[a-zA-Z0-9./:.]
		photo_url = str(re.search('[htps:/]{7,8}[a-zA-Z0-9._/:.]+[a-zA-Z0-9./:.-]+', search_string).group())
		if photo_url[-4:]!=".jpg":
			print "Redirect suspected."
			photo_url = photo_url+".jpg"
		print "URL: {}".format(photo_url)
		
		photo_name = re.findall(r'(>)([\w\s,().{}\[\]]+)(<?)',search_string)
		print "List: {}".format(photo_name)
		photo_name = photo_name[0][1]+".jpg"
		urllib.urlretrieve(photo_url, photo_name)
		print "Name: {}\n".format(photo_name)
		if image_check(photo_name):
			a = apply_background(photo_name)
			print "Applied."
		else:
			print "A redirect URL found. Image is not downloaded properly."
	else:
		print "Something went wrong!"
		print r.status_code

calling("Wallpapers")

#<a class="title may-blank " href="http://newbusinesstips.com/wp-content/uploads/2015/12/Wallpaper-1.jpg" tabindex="1">Beautiful Valley View[2560x1440]</a>