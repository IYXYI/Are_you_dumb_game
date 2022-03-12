import tkinter
from tkinter import *
from random import randint


gui = Tk()

gui.title("Are you dumb")
gui.geometry("500x200")


var = StringVar()
padx_var = IntVar()
pady_var = IntVar()

padx_var = 450
pady_var = 100
var.set("Are you dumb ?")

def msgCallBack():
    padx_var = randint(1,400)
    pady_var = randint(1, 150)
    btn1.place(x = padx_var, y = pady_var)
    
def Iknewit():
    var.set("I know it ;) LOL")
    label = Label(gui, textvariable=var, relief=FLAT)

label = Label(gui, textvariable=var, relief=RAISED)



btn1 = Button(
	gui,
	text = "NO",
	command = msgCallBack, 
	activeforeground = "green",
	activebackground = "yellow",
	padx = 8,
	pady = 5
)

btn2 = Button(
	gui,
	text = "YES",
    command = Iknewit, 
	activeforeground = "blue",
	activebackground = "yellow",
	padx = 8,
	pady = 5
)


label.pack()

btn1.place(x = padx_var, y = pady_var)
btn2.place(x=10, y=100)


gui.mainloop()