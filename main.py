from tkinter import *
from addDevicePage import addDevice
from deleteDevicePage import deleteDevice
from addDeviceHistory import edithistory
from searchPage import search
from repairsPage import repairWindow
import sendNotify as SN

SN.send()

# this is main page
root = Tk()
root.title("cleopatra Hospital")
root.geometry('400x400')
root.iconbitmap(".\\Images\\Hospital.ico")

add_button_image = PhotoImage(file=r'.\\Images\\add.png')
delete_button_image = PhotoImage(file=r'.\\Images\\delete.png')
search_button_image = PhotoImage(file=r'.\\Images\\search.png')
history_button_image = PhotoImage(file=r'.\\Images\\history.png')
Repairs = PhotoImage(file=r'.\\Images\\task-done.png')

label_space1 = Label(root).grid(row=2, column=0, pady=20, padx=10)
label_space2 = Label(root).grid(row=4, column=0, pady=20, padx=10)
label_space3 = Label(root).grid(row=6, column=0, pady=20, padx=10)
label_space4 = Label(root).grid(row=8, column=0, pady=20, padx=10)

# this variable hold the button add device
buttonAddDevice = Button(root, command=addDevice, image=add_button_image, borderwidth=0).grid(row=1, column=0)

buttonDeleteDevice = Button(root, command=deleteDevice, image=delete_button_image, borderwidth=0, text="Delete device",
                            bg="LightBlue1").grid(
    row=1, column=2)

buttonAddHistory = Button(root, command=edithistory, image=history_button_image, borderwidth=0,
                          bg="LightBlue1", ).grid(row=3,
                                                  column=0)

buttonSearchDevice = Button(root, command=search, text="Search device", image=search_button_image, borderwidth=0,
                            bg="LightBlue1").grid(row=3, column=2)

buttonPrintRepairs = Button(root, command=repairWindow, text="get task", borderwidth=0,
                            bg="LightBlue1", image=Repairs).grid(row=5, column=0)

root.mainloop()
