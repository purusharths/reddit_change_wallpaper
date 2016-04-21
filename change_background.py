#!/usr/bin/env python
import ctypes
import os

class apply_background():
	"""docstring for apply_background"""
	image_name = ""
	def __init__(self, todays_date):
		self.image_name = todays_date
		self.apply()

	def apply(self):
		path = os.getcwd()
		drive = path[:3]
		folder = path[3:]
		
		image = self.image_name
		image_path = os.path.join(drive, folder, image)
		SPI_SETDESKWALLPAPER = 20 
		ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
		print "."

class apply_background_linux():
	def __init__(self, name):
		print "..."
		self.apply(name)
	
	def apply(self, name):
		cwd = os.getcwd()
		wallpaper_name = '"{}"'.format(name)
		cwd = 'file://'+cwd+"/"+wallpaper_name
		print cwd
		os.system("gsettings set org.gnome.desktop.background picture-uri "+cwd)


#os.system("gsettings set org.gnome.desktop.background picture-uri "+path)
