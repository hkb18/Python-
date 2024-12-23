# import tkinter
from tkinter import *

# windows = tkinter.Tk()
windows = Tk()
windows.title("My First GUI Pgm")
windows.minsize(width=500, height=300)
windows.config(padx=90, pady=90)

# LABEL

# my_label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# BUTTON

def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# button = tkinter.Button(text="Click Me", command=button_click)
button = Button(text="Click Me", command=button_click)
button.pack()

# ENTRY

input = Entry(width=16)
input.insert(END, string="Enter something")
print(input.get())
input.pack()

# TEXTBOX
text = Text(height=5, width=30)
text.focus()  # Puts cursor in textbox
text.focus()
text.insert(END, "Multi-line text entry")
print(text.get("1.0", END))  # Gets current value in textbox at line 1, character 0
text.pack()


# Spinbox

def spinbox_used():
    print(spinbox.get())  # gets current value in spinbox


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# SCALE

def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CHECKBOX
def checkbox_used():
    print(checked_state.get())  # Prints 1 if ON button checked, otherwise 0


# variables to hold on to checked state,0 is off & 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(text="Is ON?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()


# RADIOBUTTON

def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# LISTBOX
def listbox_used(event):
    print(listbox.get(listbox.curselection()))  # Gets current selection from listbox


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for items in fruits:
    listbox.insert(fruits.index(items), items)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

windows.mainloop()

#####TODO: *args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
#  print(add(1, 2, 3, 4))


######TODO: **kwargs

# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=4)
