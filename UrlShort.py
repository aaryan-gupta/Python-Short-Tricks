import pyshorteners # pip install pyshorteners
from tkinter import *

def url():
	shortener = pyshorteners.Shortener()
	x = shortener.tinyurl.short(urlValue.get())
	label.config(text=x)
	root.clipboard_clear()
	root.clipboard_append(x)

root = Tk()
root.geometry("500x500")

urlValue = StringVar()

Label(root, text="URL Shortener", fg="#FF9DAB", font="poppins 20", bg="black",pady="10").pack(fill=X)
Entry(root, textvariable=urlValue, width="40").pack(pady="20")
Button(root, text="Generate URL", command=url, bg="black", fg="white", font="poppins 10",padx="15", pady="5", relief=SUNKEN).pack(pady="10")

label = Label(root)
label.pack()

root.mainloop()