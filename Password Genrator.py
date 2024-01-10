import random
from tkinter import *
from tkinter.ttk import *

def low():
	entry.delete(0, END)
	l = var1.get()
	lwr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
	passwd = ""

	if var.get() == 1:
		for i in range(0, l):
			passwd = passwd + random.choice(lwr)
		return passwd

	elif var.get() == 0:
		for i in range(0, l):
			passwd = passwd + random.choice(upper)
		return passwd

	elif var.get() == 3:
		for i in range(0, l):
			passwd = passwd + random.choice(digits)
		return passwd
	
	else:
		print("Please choose any option")

def generate():
	passwd1 = low()
	entry.insert(10, passwd1)
	
s = Tk()
var = IntVar()
var1 = IntVar()

s.title("Password Generator")
Rand_passwd = Label(s, text="Password")
Rand_passwd.grid(row=0)
entry = Entry(s)
entry.grid(row=0, column=1)

c_label = Label(s, text="Length")
c_label.grid(row=1)

generate_button = Button(s, text="Generate Password",width=40, command=generate)
generate_button.grid(row=0, column=3)

p_low = Radiobutton(s, text="Low", variable=var, value=1)
p_low.grid(row=1, column=3, sticky='E')
q_middle = Radiobutton(s, text="Medium", variable=var, value=0)
q_middle.grid(row=1, column=4, sticky='E')
r_strong = Radiobutton(s, text="Strong", variable=var, value=3)
r_strong.grid(row=1, column=5, sticky='E')
c = Combobox(s, textvariable=var1)

c['values'] = (6,7,8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20)
c.current(0)
c.bind('<<ComboboxSelected>>')
c.grid(column=1, row=1)
s.mainloop()