import mysql.connector
from tkinter import *
from prettytable import PrettyTable
# pip install mysql-connector prettytable

root = Tk()

con = mysql.connector.connect(host="localhost", user="root", password="", db="tkinter")
cursor = con.cursor()

string = ""
myTable = PrettyTable(["Name", "Birthday Date"])

def getvals():
	if(len(nameValue.get()) != 0 and len(dateValue.get()) != 0):
		cursor.execute(f"insert into birthday (name, birthday) values ('{nameValue.get()}', '{dateValue.get()}')")
		con.commit()

def show():
	myTable = PrettyTable(["Name", "Birthday Date"])
	global string
	cursor.execute("select * from birthday")
	myresult = cursor.fetchall()
	for x in myresult:
		x = list(x)
		print(x)
		myTable.add_row(x)
	print("Query Executed successfully")
	label.config(text=str(myTable))

root.title("Birthday App")
root.geometry("300x300")

nameValue = StringVar()
dateValue = StringVar()

Label(root, text="Name").pack()
Entry(root, textvariable=nameValue).pack()

Label(root, text="Date").pack()
Entry(root, textvariable=dateValue).pack()

label = Label(root)
Button(text="Add Record", command=getvals).pack()
Button(text="Show Records", command=show).pack()
label.pack()

root.mainloop()