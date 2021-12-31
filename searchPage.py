from tkinter import *
from tkinter import messagebox
from GeneralMethods import searchLabelsData
from functools import partial


def search():
    root = Tk()
    root.geometry("500x500")
    root.title("search device")
    label_serial = Label(root, text="Serial ").grid(row=0, column=0, sticky=E)
    serial_entry = Entry(root)
    serial_entry.grid(row=0, column=1)

    labels = []
    # label print name
    name = Label(root, text="Device Name is : ")
    name.grid(row=1, column=0, sticky=E)

    name1 = Label(root, text="NOT FOUND")
    name1.grid(row=1, column=1)
    labels.append(name1)

    # label to model
    label_model = Label(root, text="Model Type : ")
    label_model.grid(row=2, column=0, sticky=E)

    # label to model
    label_model1 = Label(root, text="NOT FOUND")
    label_model1.grid(row=2, column=1)
    labels.append(label_model1)

    # label to department
    label_department = Label(root, text="Department : ")
    label_department.grid(row=3, column=0, sticky=E)

    # label to department
    label_department1 = Label(root, text="NOT FOUND")
    label_department1.grid(row=3, column=1)
    labels.append(label_department1)

    # label to floor
    label_floor = Label(root, text="Floor No : ")
    label_floor.grid(row=4, column=0, sticky=E)

    # label to floor
    label_floor1 = Label(root, text="NOT FOUND")
    label_floor1.grid(row=4, column=1)
    labels.append(label_floor1)

    # label to manufacture
    label_manufacture = Label(root, text="Manufacture : ")
    label_manufacture.grid(row=5, column=0, sticky=E)

    # label to manufacture
    label_manufacture1 = Label(root, text="NOT FOUND")
    label_manufacture1.grid(row=5, column=1)
    labels.append(label_manufacture1)

    # label to agent
    label_agent = Label(root, text="Agent : ")
    label_agent.grid(row=6, column=0, sticky=E)

    # label to agent
    label_agent1 = Label(root, text="NOT FOUND")
    label_agent1.grid(row=6, column=1)
    labels.append(label_agent1)

    # label to serial
    label_serial = Label(root, text="Serial No : ")
    label_serial.grid(row=7, column=0, sticky=E)

    # label to serial
    label_serial1 = Label(root, text="NOT FOUND")
    label_serial1.grid(row=7, column=1)
    labels.append(label_serial1)

    # label to warranty_period
    label_warranty_period = Label(root, text="Warranty Period : ")
    label_warranty_period.grid(row=8, column=0, sticky=E)

    # label to warranty_period
    label_warranty_period1 = Label(root, text="NOT FOUND")
    label_warranty_period1.grid(row=8, column=1)
    labels.append(label_warranty_period1)

    # label to Periodic_maintenanceschedule
    label_periodic_maintenance = Label(root, text="Periodic Maintenance Schedule : ")
    label_periodic_maintenance.grid(row=9, column=0, sticky=E)

    # label to Periodic_maintenanceschedule
    label_periodic_maintenance1 = Label(root, text="NOT FOUND")
    label_periodic_maintenance1.grid(row=9, column=1)
    labels.append(label_periodic_maintenance1)

    # label to Installation_commissioning_date
    label_installation = Label(root, text="Installation date : ")
    label_installation.grid(row=10, column=0, sticky=E)

    # label to Installation_commissioning_date
    label_installation1 = Label(root, text="NOT FOUND")
    label_installation1.grid(row=10, column=1)
    labels.append(label_installation1)

    # label to Periodic_maintenanceschedule
    label_ppm_period = Label(root, text="PPM Period : ")
    label_ppm_period.grid(row=11, column=0, sticky=E)

    # label to Periodic_maintenanceschedule
    label_ppm_period1 = Label(root, text="NOT FOUND")
    label_ppm_period1.grid(row=11, column=1)
    labels.append(label_ppm_period1)

    # label to Periodic_maintenanceschedule
    label_First_ppm = Label(root, text="1st PPM : ")
    label_First_ppm.grid(row=12, column=0, sticky=E)

    # label to Periodic_maintenanceschedule
    label_First_ppm1 = Label(root, text="NOT FOUND")
    label_First_ppm1.grid(row=12, column=1)
    labels.append(label_First_ppm1)

    # label to Periodic_maintenanceschedule
    label_Second_ppm = Label(root, text="2nd PPM : ")
    label_Second_ppm.grid(row=13, column=0, sticky=E)

    # label to Periodic_maintenanceschedule
    label_Second_ppm1 = Label(root, text="NOT FOUND")
    label_Second_ppm1.grid(row=13, column=1)
    labels.append(label_Second_ppm1)

    # label to Periodic_maintenanceschedule
    label_Third_ppm = Label(root, text="3rd PPM : ")
    label_Third_ppm.grid(row=14, column=0, sticky=E)

    # label to Periodic_maintenanceschedule
    label_Third_ppm1 = Label(root, text="NOT FOUND")
    label_Third_ppm1.grid(row=14, column=1)
    labels.append(label_Third_ppm1)

    # label to Periodic_maintenanceschedule
    label_Fourth_ppm = Label(root, text="4th PPM : ")
    label_Fourth_ppm.grid(row=15, column=0, sticky=E)

    # label to Periodic_maintenanceschedule
    label_Fourth_ppm1 = Label(root, text="NOT FOUND")
    label_Fourth_ppm1.grid(row=15, column=1)
    labels.append(label_Fourth_ppm1)

    label_space = Label(root).grid(row=0, column=2)
    label_space1 = Label(root).grid(row=0, column=3)
    label_space1 = Label(root).grid(row=0, column=4)

    msg = messagebox
    button = Button(root, text="get info", bg="LightBlue", font=("Arial", 10),
                    command=partial(searchLabelsData, serial_entry, labels, msg))
    button.grid(row=0, column=5)
