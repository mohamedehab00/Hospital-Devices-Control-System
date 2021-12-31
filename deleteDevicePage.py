from tkinter import *
from GeneralMethods import delete_device
from functools import partial
from tkinter import messagebox


def deleteDevice():
    root = Tk()
    root.geometry("500x150")
    root.title("Delete Device")

    label = Label(root, text="Serial ").grid(row=0, column=0, sticky=E)

    delete_entry = Entry(root, width=40)
    delete_entry.grid(row=0, column=1)

    label_space = Label(root)
    label_space.grid(row=1, column=1)

    msg = messagebox
    Button_get_deleted = Button(root, text="delete serial", bg="LightBlue", font=("Arial", 10),
                                command=partial(delete_device, delete_entry, msg)).grid(row=2,
                                                                                        column=1)
