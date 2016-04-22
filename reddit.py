#!/usr/bin/env python
import re
import urllib
import platform

import requests
from bs4 import BeautifulSoup
from PIL import Image
import imgur_album as album
platform = platform.system()
print platform
try:
	if platform.lower() == 'windows':
		from change_background import apply_background as background
	if platform.lower() == 'linux':
		from change_background import apply_background_linux as background
except:
	print "Import Error. Unsupported OS"
	exit()

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
		is_album = re.findall('[htps:/]+imgur.com/a/[a-zA-Z0-9./]+', photo_url)
		if is_album:
			print "Imgur album detected. Downloading first photo of the album..."
			photo_url = album.get_album_photos(photo_url)

		if photo_url[-4:]!=".jpg":
			print "Redirect suspected."
			photo_url = photo_url+".jpg"
		print "URL: {}".format(photo_url)
		
		photo_name = re.findall(r"(>)([\w\s,().'{}\[\]]+)(<?)",search_string)
		photo_name = photo_name[0][1]+".jpg"
		
		print "List: {}".format(photo_name)
		urllib.urlretrieve(photo_url, photo_name)
		print "Name: {}\n".format(photo_name)
		if image_check(photo_name):
			##
			print "\n\n{}".format(photo_name)
			##
			a = background(photo_name)
			print "Applied."
		else:
			print "Image is not downloaded properly."
	else:
		print "Something went wrong!"
		print r.status_code

calling("Wallpapers")

#<a class="title may-blank " href="http://newbusinesstips.com/wp-content/uploads/2015/12/Wallpaper-1.jpg" tabindex="1">Beautiful Valley View[2560x1440]</a>
