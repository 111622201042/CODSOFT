from tkinter import *
import random

s = Tk()
s.geometry("650x450")
s.title("Rock Paper Scissor Game")
cmpt_val = {
	"0": "Rock",
	"1": "Paper",
	"2": "Scissor"
}

def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text="Player                   ")
	l3.config(text="Computer")
	l4.config(text="")


def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"


def isrock():
	cv = cmpt_val[str(random.randint(0, 2))]
	if cv == "Rock":
		result= "Match Draw"
	elif cv == "Scissor":
		result = "Player Win"
	else:
		result = "Computer Win"
	l4.config(text=result)
	l1.config(text="Rock		 ")
	l3.config(text=cv)
	button_disable()

def ispaper():
	cv = cmpt_val[str(random.randint(0, 2))]
	if cv == "Paper":
		result = "Match Draw"
	elif cv == "Scissor":
		result = "Computer Win"
	else:
		result = "Player Win"
	l4.config(text=result)
	l1.config(text="Paper		 ")
	l3.config(text=cv)
	button_disable()

def isscissor():
	cv = cmpt_val[str(random.randint(0, 2))]
	if cv == "Rock":
		result = "Computer Win"
	elif cv == "Scissor":
		result = "Match Draw"
	else:
		result = "Player Win"
	l4.config(text=result)
	l1.config(text="Scissor		 ")
	l3.config(text=cv)
	button_disable()

Label(s,text="Rock Paper Scissor",font="normal 20 bold",fg="blue",bg="lightblue").pack(pady=20)

frame = Frame(s)
frame.pack()

l1 = Label(frame,text="Player			 ",font=10)
l2 = Label(frame,text="VS			 ",font="normal 10 bold",fg="red")
l3 = Label(frame, text="Computer", font=10)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
l4 = Label(s,text="",font="normal 20 bold",bg="Gold",width=20,borderwidth=2,relief="solid")
l4.pack(pady=20)

frame1 = Frame(s)
frame1.pack()

b1 = Button(frame1, text="Rock",font=10, width=10,fg="white",bg="grey",command=isrock)
b2 = Button(frame1, text="Paper ",font=10, width=10,fg="white",bg="grey",command=ispaper)
b3 = Button(frame1, text="Scissor",font=10, width=10,fg="white",bg="grey",command=isscissor)

b1.pack(side=LEFT, padx=40)
b2.pack(side=LEFT, padx=40)
b3.pack(padx=40)

Button(s, text="Reset Game",font=20,width="20", fg="black",bg="red", command=reset_game).pack(pady=50)
s.mainloop()