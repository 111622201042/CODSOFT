from tkinter import *
win = Tk() 
win.geometry("312x324") 
win.resizable(0, 0)  
win.title("Calculator")

def btn_click(item):
    global exp
    exp = exp + str(item)
    input_text.set(exp)

def bt_clear(): 
    global exp
    exp = "" 
    input_text.set("")
 
def bt_equal():
    global exp
    result = str(eval(exp)) 
    input_text.set(result)
    expr = ""
 
exp = ""
input_text = StringVar()
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) 
 
btn_frame = Frame(win, width=312, height=272.5, bg="lightblue")
btn_frame.pack()
 

clear_Button = Button(btn_frame, text = "C", fg = "black", width = 21, height = 3, bd = 0, bg = "red", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
 
one_Button = Button(btn_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 1, column = 0, padx = 1, pady = 1) 
two_Button = Button(btn_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 1, column = 1, padx = 1, pady = 1)
three_Button = Button(btn_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(3)).grid(row =1, column = 2, padx = 1, pady = 1)
 
four_Button = Button(btn_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five_Button = Button(btn_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six_Button = Button(btn_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
seven_Button = Button(btn_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
eight_Button = Button(btn_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine_Button = Button(btn_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "grey", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
 

plus_Button = Button(btn_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 0, column =2, padx = 1, pady = 1)
minus_Button = Button(btn_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 0, column = 3, padx = 1, pady = 1)
multiply_Button = Button(btn_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
divide_Button = Button(btn_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 2, column = 3, padx = 1, pady = 1)
Modulo_Button=Button(btn_frame,text="%",fg="black", width = 10, height = 3, bd = 0, bg = "blue", cursor = "hand2", command = lambda: btn_click("%")).grid(row = 3, column = 3, padx = 1, pady = 1)

zero_Button = Button(btn_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point_Button = Button(btn_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1) 
equals_Button = Button(btn_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
win.mainloop()