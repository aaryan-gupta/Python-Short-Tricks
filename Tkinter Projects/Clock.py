from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")
def time():
	string = strftime("%H : %M : %S %p %d %m %Y")
	label.config(text=string)
	label.after(1000, time)

label = Label(root, font=("Poppins", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()
root.mainloop()