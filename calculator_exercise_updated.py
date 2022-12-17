#Used previously built calculator
#Improved the look and added additional button

#Learned more math equations
#Came back and added additional buttons, that vary in the way they act

from tkinter import *

root = Tk()
root.title("Simple Little Calculator")

e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_delete():
    e.delete(0, END)

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    # a ** b = Elevates a to the power of b. For non integer values of b, this becomes a root (i.e. a**(1/2) is the square root of a)
    # a // b = The integer part of the integer division of a by b
    # a % b = The remainder part of the integer division of a by b
    # to calculate the square root of a number x, you can use x**(1/2).

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

    if math == "power of":
        e.insert(0, f_num ** int(second_number))


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_power_of():
    first_number = e.get()
    global f_num
    global math
    math = "power of"
    f_num = int(first_number)
    e.delete(0, END)

def button_square_root():
    first_number = e.get()
    global f_num
    global math
    math = "square root"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0, f_num ** (1 / 2))
    #made this button show result w/o using "="


#Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

    #Mac does not support the changing of background colors on buttons
    #Can instead highlight the background
button_clear = Button(root, text="Clear", padx=28, pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=102, pady=20, command=button_equal, highlightbackground="white")
button_delete = Button(root, text="<-", padx=36, pady=20, command=button_delete)

button_plus = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

button_power_of = Button(root, text="^", padx=41, pady=20, command=button_power_of)
button_square_root = Button(root, text="Sq", padx=35, pady=20, command=button_square_root)

#Put the buttons on the screen
button_clear.grid(row=1, column=0)
button_delete.grid(row=1, column=1)
button_square_root.grid(row=1, column=2)
button_power_of.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)

button_0.grid(row=5, column=0)

button_equal.grid(row=5, column=1, columnspan=2)
button_plus.grid(row=5, column=3)


root.mainloop()