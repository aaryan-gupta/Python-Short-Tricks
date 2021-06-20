from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from textblob import TextBlob # pip install textblob
root = Tk()
root.geometry("500x500")
root.title("Translator")

langD = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 
'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

# combo box
languages = StringVar()
font_box = Combobox(root, width=30, textvariable=languages, state="readonly")
font_box['values'] = [e for e in langD.keys()]
font_box.current(37)
font_box.place(x=300, y=0)

def tt():
	try:
		word = TextBlob(varName1.get())
		lan = word.detect_language()
		lanToD = languages.get()
		lanTo = langD[lanToD]
		word = word.translate(from_lang=lan, to=lanTo)
		# sp = word.split()
		label3.configure(text=word)
		varName2.set(word)
	except:
		varName2.set("Try another keyword")

def mainExit():
	rr = messagebox.askyesnocancel("Notification", "Are you want to EXIT!", parent=root)
	if rr == True:
		root.destroy()

root.configure(bg="green")

varName1 = StringVar()
entry1 = Entry(root, width=30, textvariable=varName1, font="poppins 14 italic bold" )
entry1.place(x=150, y=40)

varName2 = StringVar()
entry1 = Entry(root, width=30, textvariable=varName2, font="poppins 14 italic bold" )
entry1.place(x=150, y=80)

label1 = Label(root, text="Enter Words: ", font="poppins 15 italic bold")
label1.place(x=5, y=40)

label2 = Label(root, text="Translated: ", font="poppins 15 italic bold")
label2.place(x=5, y=80)

label3 = Label(root, text=" ", font="poppins 15 italic bold")
label3.place(x=5, y=250)

btn1 = Button(root, text="click",command=tt, bd=10, bg="lightblue", activebackground="red", width="10", font="poppins 15 italic bold")
btn1.place(x=70, y=170)

btn2 = Button(root, text="exit",command=mainExit, bd=10, bg="lightblue", activebackground="red", width="10", font="poppins 15 italic bold")
btn2.place(x=280, y=170)

root.mainloop()