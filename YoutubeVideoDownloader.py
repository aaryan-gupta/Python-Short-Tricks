import pytube # pip install pytube
url = '' # Enter the youtube video link
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download('/Downloads') # In Other Folder