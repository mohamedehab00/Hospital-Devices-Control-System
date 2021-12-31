import tkinter
import ExcelOperations as exc
from LogOperations import editLogFile
import dateutil.parser as parser
import numpy as np
from tkinter import messagebox


def empty_entry(entry):
    entry.delete(0, len(entry.get()))
    entry.insert(0, "")


def get_data(entries, msg):
    try:
        entries_data = [e.get() for e in entries]
        data = {}
        if "" in entries_data:
            raise FutureWarning

        if not exc.check_no_duplicated_serial(entries_data[exc.DB_Cols.index("SerialNo")]):
            raise ValueError

        valid = True
        for i, entry in enumerate(entries_data):
            if i == exc.DB_Cols.index("ppmPeriod") or i == exc.DB_Cols.index("WarrantyPeriod"):
                try:
                    int(entry)
                except ValueError:
                    valid = False
                    msg.showerror("Error", "PPM Period & Warranty must be period of Months!!!")
            if not valid:
                break
            data[exc.DB_Cols[i]] = entry
        if valid:
            step = 12 // int(data["ppmPeriod"])
            date = parser.parse(data["PPM"])
            i = 0
            if step > 0:
                quarters = ["first", "second", "third", "fourth"]
                dates = np.arange(date.isoformat(), 12, step=step, dtype='datetime64[M]')
                for date in dates:
                    data[quarters[i] + "PPM"] = date.astype(object).strftime("%B")
                    i += 1
            exc.insertRecord(data)
            for entry in entries:
                empty_entry(entry)
            msg.showinfo("add device", "device added")
    except ValueError:
        msg.showerror("Error", "SerialNo. is Duplicated!!!")
    except FutureWarning:
        msg.showerror("Error", 'Must complete all fields')


def delete_device(entry, msg):
    try:
        if entry.get() == "":
            raise FutureWarning

        elif exc.checkSerialExist(entry.get())[0]:
            raise ValueError
        else:
            exc.deleteRecord(entry.get())
            empty_entry(entry)
        msg.showinfo("deleted device", "device is deleted")
    except FutureWarning:
        msg.showerror("Error", "Must enter the serial")
    except ValueError:
        msg.showerror("Error", "serial not exist")


def edit_history_info(serial, entries):
    dataLabels = ["Start Date", "End Date", "Name", "Description"]
    data = {}
    for i, entry in enumerate(entries):
        if i == len(entries) - 1:
            data[dataLabels[i]] = entry.get("0.0", "end-1c")
        else:
            data[dataLabels[i]] = entry.get()
    msg = messagebox
    editLogFile(serial, data, msg)
    for i in range(len(entries)):
        if i == len(entries) - 1:
            entries[i].delete('0.0', tkinter.END)
            entries[i].insert('0.0', "")
        else:
            empty_entry(entries[i])


def setSearchLabels(labels, data):
    for i, label in enumerate(labels):
        label.config(text=data[exc.DB_Cols[i]])


def searchLabelsData(Entry, labels, msg):
    serial = Entry.get()
    cond, data = exc.searchRecord(serial)
    if cond:
        setSearchLabels(labels, data)

    else:
        setSearchLabels(labels, data)
        msg.showerror("Error", "Serial Not Found")
