import instaloader # pip install instaloader
profile = "" # Enter Instagram ID to download profile picture
print(instaloader.Instaloader().download_profile(profile, profile_pic_only=True))