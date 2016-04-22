Change your desktop wallpaper to reddit's `/r/wallpapers` subreddit's top wallpaper.<br/>
If you're on windows, before running this execute:<br/>
`C:\Python27\Scripts\pip.exe install ctypes bs4 PIL`<br/>
For linux:<br/>
`sudo pip install bs4 PIL`
<br/><br/>
run `reddit.py` <br/>
<br/>
By default, if the link to the top wallpaper is of an imgur album, First photo of the album will be downloaded.<br/>
To change this to a random photo from the album, change the value inside `random_wallpaper.txt` from `0` to `1`.<br/><br/>

If you want to download an entire Imgur album, run:
`imgur_album.py`<br/>
It will download all the photos in the current directory album with a random number as name.
