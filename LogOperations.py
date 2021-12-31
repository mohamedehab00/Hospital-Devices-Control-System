from datetime import datetime
import os

Main_LOG_Folder_Name = ".\\LogFiles\\"


def createLogFile(data):
    with open(Main_LOG_Folder_Name + str(data["SerialNo"] + ".log"), 'a') as file:
        dateTime = datetime.now()
        file.write("Device : " + data["DeviceName"] + "\n" + "Model : " + data["ModelType"] + "\n" + "Serial : " + \
                   data["SerialNo"] + "\n" + "Manufacture : " + data[
                       "Manufacture"] + "\n" + "Device History : \n\nDevice Added... "
                   + dateTime.strftime("%d-%m-%Y %H:%M:%S"))


def editLogFile(serial, data, msg):
    with open(Main_LOG_Folder_Name + str(serial) + ".log", 'a') as file:
        dateTime = datetime.now()
        file.write("\n\nDevice History Added... " + dateTime.strftime("%d-%m-%Y %H:%M:%S") + "\n" + \
                   "Start Date : " + data["Start Date"] + "  End Date : " + data["End Date"] + "\n" \
                   + "Name : " + data["Name"] + "\n" \
                   + "Description : \n" + data["Description"])
        msg.showinfo("Done", "History Added!!!")


def openLogFile(serial):
    os.startfile(Main_LOG_Folder_Name + serial + ".log")
