#######################################
# Basic arithmetic calculator program #
#           LAB 1 PART C              #
#######################################

from tkinter import *
import parser

root = Tk()
root.title('Calculator')

i = 0
def clear_all():
    """Clears the calculator"""
    display.delete(0, END)

def get_variables(num):
    """Gets the user input"""
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    """Gets the users chosen operation"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def calculate():
    """Calculates the equation and returns a value to the screen"""
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")

# Create the rows and columns
for i in range(3):
    root.columnconfigure(i, pad=3)

for i in range(3):
    root.rowconfigure(i, pad=3)

display = Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 4    , sticky = W+E)

# loop the first 9 buttons(1-9)
buttons = []
for i in range(0, 10):
    button = Button(root, text = str(i), font=("Calibri", 12), command = lambda num=i : get_variables(num))
    buttons.append(button)

# Operation Buttons
cls = Button(root, text = "AC", command = clear_all, font=("Calibri", 12), foreground = "red")
buttons.append(cls)
zero = Button(root, text = "0", command = lambda : get_variables(0), font=("Calibri", 12))
buttons.append(zero)
result = Button(root, text = "=", command = calculate, font=("Calibri", 12), foreground = "red")
buttons.append(result)
plus = Button(root, text = "+", command =  lambda : get_operation("+"), font=("Calibri", 12))
buttons.append(plus)
minus = Button(root, text = "-", command =  lambda : get_operation("-"), font=("Calibri", 12))
buttons.append(minus)
multiply = Button(root,text = "*", command =  lambda : get_operation("*"), font=("Calibri", 12))
buttons.append(multiply)
divide = Button(root, text = "/", command = lambda :  get_operation("/"), font=("Calibri", 12))
buttons.append(divide)

#Plot the buttons
buttons[1].grid(row=2, column=0)
buttons[2].grid(row=2, column=1)
buttons[3].grid(row=2, column=2)
buttons[4].grid(row=3, column=0)
buttons[5].grid(row=3, column=1)
buttons[6].grid(row=3, column=2)
buttons[7].grid(row=4, column=0)
buttons[8].grid(row=4, column=1)
buttons[9].grid(row=4, column=2)
buttons[10].grid(row=5, column=0)
buttons[11].grid(row=5, column=1)
buttons[12].grid(row=5, column=2)

buttons[13].grid(row=2, column=3)
buttons[14].grid(row=3, column=3)
buttons[15].grid(row=4, column=3)
buttons[16].grid(row=5, column=3)

root.mainloop()
