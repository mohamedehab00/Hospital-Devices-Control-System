from tkinter import *
from functools import partial
from tkinter import messagebox
from GeneralMethods import edit_history_info
from ExcelOperations import checkSerialExist
from LogOperations import openLogFile
from tkcalendar import DateEntry


def get_serial(entry, msg):
    try:
        if entry.get() == "" or checkSerialExist(entry.get())[0]:
            raise ValueError
        else:
            create_new_page(entry.get())
    except ValueError:
        msg.showerror("Error", "Must enter the serial")


def edithistory():
    root = Tk()
    root.geometry("500x500")
    root.title("Edit Device")

    label = Label(root, text="Serial you want to add to history : ")
    label.grid(row=0, column=0, sticky=E)

    entry = Entry(root, width=40)
    entry.grid(row=0, column=1)

    msg = messagebox
    button_get_serial = Button(root, text="Edit history", bg="LightBlue", font=("Arial", 10),
                               command=partial(get_serial, entry, msg))
    button_get_serial.grid(row=1, column=1)
    button_print_history = Button(root, text="print history", bg="LightBlue", font=("Arial", 10),
                                  command=partial(print_history, entry, msg))
    button_print_history.grid(row=2, column=1)


def create_new_page(serial):
    entries_history = []

    root = Tk()
    root.geometry("750x750")
    root.title("History")

    label_start_date = Label(root, text="Start Date :")
    label_start_date.grid(row=0, column=0, sticky=E)
    cal = DateEntry(root, width=12, background='darkblue', foreground='white', sticky=E)
    cal.grid(row=0, column=1, pady=7)
    entries_history.append(cal)

    label_finish_date = Label(root, text="Finish Date :")
    label_finish_date.grid(row=1, column=0, sticky=E)
    cal1 = DateEntry(root, width=12, background='darkblue', foreground='white', sticky=E)
    cal1.grid(row=1, column=1, pady=7)
    entries_history.append(cal1)

    label_name = Label(root, text="Name :").grid(row=2, column=0, sticky=E)
    name_entry = Entry(root, width=50)
    name_entry.grid(row=2, column=1, pady=25)
    entries_history.append(name_entry)

    lable_action = Label(root, text="Description :")
    lable_action.grid(row=3, column=0, sticky=E)
    description = Text(root, width=60, height=5)
    description.grid(row=3, column=1)
    entries_history.append(description)

    label_space = Label(root)
    label_space.grid(row=5, column=1)

    msg = messagebox
    button_get_history_data = Button(root, bg="LightBlue", font=("Arial", 10),
                                     command=partial(edit_history_info, serial, entries_history), text="Add history")

    button_get_history_data.grid(row=6, column=1)

def print_history(entry, msg):
    try:
        if entry.get() == "":
            raise ValueError
        else:
            openLogFile(entry.get())
    except ValueError:
        msg.showerror("Error", "Serial Not Found!!!")
