from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from GeneralMethods import get_data
from functools import partial


def addDevice():
    addDeviceEntries = []

    root = Tk()
    root.title("Add Device")
    root.geometry("500x450")

    # label print name
    label_name = Label(root, text="Device Name ")
    label_name.grid(row=0, column=0, sticky=E)

    # input name
    name = Entry(root, width=40)
    name.grid(row=0, column=1, pady=7)
    addDeviceEntries.append(name)

    # label to model
    label_model = Label(root, text="Model Type ")
    label_model.grid(row=1, column=0, sticky=E)

    # input model
    model = Entry(root, width=40)
    model.grid(row=1, column=1, pady=7)
    addDeviceEntries.append(model)

    # label to department
    label_department = Label(root, text="Department ")
    label_department.grid(row=2, column=0, sticky=E)

    # input department
    depart = Entry(root, width=40)
    depart.grid(row=2, column=1, pady=7)
    addDeviceEntries.append(depart)

    # label to floor
    label_floor = Label(root, text="Floor No. ")
    label_floor.grid(row=3, column=0, sticky=E)

    # input floor
    floor = Entry(root, width=40)
    floor.grid(row=3, column=1, pady=7)
    addDeviceEntries.append(floor)

    # label to manufacture
    label_manufacture = Label(root, text="Manufacture ")
    label_manufacture.grid(row=4, column=0, sticky=E)

    # input manufactury
    manufacture = Entry(root, width=40)
    manufacture.grid(row=4, column=1, pady=7)
    addDeviceEntries.append(manufacture)

    # label to agent
    label_agent = Label(root, text="Agent ")
    label_agent.grid(row=5, column=0, sticky=E)

    # input agent
    agent = Entry(root, width=40)
    agent.grid(row=5, column=1, pady=7)
    addDeviceEntries.append(agent)

    # label to serial
    label_serial = Label(root, text="Serial No. ")
    label_serial.grid(row=6, column=0, sticky=E)

    # input serial and must be checked because no dupliaction
    serial = Entry(root, width=40)
    serial.grid(row=6, column=1, pady=7)
    addDeviceEntries.append(serial)

    # label to warranty_period
    label_warranty_period = Label(root, text="Warranty Period ")
    label_warranty_period.grid(row=7, column=0, sticky=E)

    # input warranty period
    warranty_period = Entry(root, width=40)
    warranty_period.grid(row=7, column=1, pady=7)
    addDeviceEntries.append(warranty_period)

    # label to Periodic_maintenanceschedule
    label_periodic_maintenance = Label(root, text="PPM ")
    label_periodic_maintenance.grid(row=8, column=0, sticky=E)

    # input Periodic maintenance schedule
    cal_PPM = DateEntry(root, width=17, background='darkblue', foreground='white', sticky=E)
    cal_PPM.grid(row=10, column=0, pady=7)
    cal_PPM.grid(row=8, column=1, pady=7)

    # label to Installation_commissioning_date
    label_installation = Label(root, text="Installation date ")
    label_installation.grid(row=9, column=0, sticky=E)

    # input Installation and commissioning date
    cal_installation = DateEntry(root, width=17, background='darkblue', foreground='white', sticky=E)
    cal_installation.grid(row=9, column=1, pady=7)
    cal_installation.grid(row=9, column=1, pady=7)
    addDeviceEntries.append(cal_installation)

    addDeviceEntries.append(cal_PPM)

    # label to Ppm_period
    label_ppm_period = Label(root, text="PPM period ")
    label_ppm_period.grid(row=10, column=0, sticky=E)

    # input Periodic maintenance schedule
    ppm_period = Entry(root, width=40)
    ppm_period.grid(row=10, column=1)
    addDeviceEntries.append(ppm_period)

    label_space = Label(root)
    label_space.grid(row=11, column=1)

    msg = messagebox
    ButtonAdd = Button(root, text="Add data", bg="LightBlue", font=("Arial", 10),
                       command=partial(get_data, addDeviceEntries, msg)).grid(row=12, \
                                                                              column=1)
