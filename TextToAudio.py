from gtts import gTTS
from playsound import playsound
# pip install gtts playsound
audio = "speech.mp3"
language = "en"
sp = gTTS(text="Enter your text which u want to convert into audio file", lang=language, slow=False)
sp.save(audio)
playsound(audio)