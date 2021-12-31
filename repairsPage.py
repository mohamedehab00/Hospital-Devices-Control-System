from tkinter import *
from tkinter import messagebox
from ExcelOperations import getUpcoming
from functools import partial


def repairWindow():
    root = Tk()
    root.geometry("500x150")
    root.title("Repairs Device")

    label = Label(root, text="Month ")
    label.grid(row=0, column=0, sticky=E)

    option = StringVar(root)
    option.set("Select an Option")
    options = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")
    menu = OptionMenu(root, option, *options)
    menu.grid(row=0, column=1)

    label_space = Label(root)
    label_space.grid(row=1, column=1)

    button_get_serial = Button(root, text="get tasks", font=("Arial", 12), bg="LightBlue1",
                               command=partial(get_devices, option))
    button_get_serial.grid(row=2, column=1)


def get_devices(entry):
    data = getUpcoming(entry.get())
    if data[0]:
        root = Tk()
        root.geometry("1000x1000")
        root.title("Upcoming Repairs")

        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)
        mylist = Listbox(root, yscrollcommand=scrollbar.set, width=1000)

        for i in data[1]:
            row = ""
            for key in i.keys():
                row += str(i[key]) + "      "
            mylist.insert(END, row)
            mylist.insert(END, "\n")
        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

    else:
        msg = messagebox
        msg.showerror("Error", "No Devices")
