import urllib.request
with open("file.txt", "wb") as f:
	f.write(urllib.request.urlopen("https://google.com/").read())
with open("file.html", "wb") as f:
	f.write(urllib.request.urlopen("https://google.com/").read())