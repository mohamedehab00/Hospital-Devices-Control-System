from datetime import datetime
import os
import GeneralMethods as GM
import pandas as pd
import ExcelOperations as EO

Main_LOG_Folder_Name = r".\\LogFiles\\"
LOG_DB_COL = ["Time", "Start Date", "End Date", "Name", "Description"]

def to_raw(string):
    return fr"{string}"

def createLogFile(serialNo):
    serialNo = str(serialNo).replace("/", "-")
    serialNo = str(serialNo).replace("\\", "-")

    if not GM.check_Exist(Main_LOG_Folder_Name, "("+serialNo+")"):
        df = pd.DataFrame(data={"Time": [], "Start Date": [], "End Date": [], "Name": [], "Description": []},
                          columns=LOG_DB_COL)
        path = to_raw(Main_LOG_Folder_Name + "(" + serialNo + ")" + ".xlsx")
        df.to_excel(path, encoding="utf-8", index=False)

def editLogFile(serial, data, msg):
    serialNew = str(serial).replace("/", "-")
    serialNew = str(serialNew).replace("\\", "-")

    createLogFile(serialNew)

    df = pd.read_excel(Main_LOG_Folder_Name+"("+serialNew+")"+".xlsx")
    df.reset_index(drop=True, inplace=True)

    date = datetime.utcnow()
    data["Time"] = date.strftime("%d-%m-%Y %H:%M:%S")

    for key in data.keys():
        data[key] = [data[key]]

    dfToAdd = pd.DataFrame(data=data, columns=LOG_DB_COL)

    df = pd.concat([df, dfToAdd], ignore_index=True)

    path = to_raw(Main_LOG_Folder_Name +"("+ serialNew +")"+ ".xlsx")

    df.to_excel(path, encoding="utf-8", index=False)

    msg.showinfo("Done", "History Added!!!")


def openLogFile(serial):
    print(EO.checkSerialExist(serial)[0])
    if EO.checkSerialExist(serial)[0]:
        raise ValueError
    else:
        serial = str(serial).replace("/", "-")
        serial = str(serial).replace("\\", "-")
        createLogFile(serial)

        path = to_raw(Main_LOG_Folder_Name + "(" + serial + ")" + ".xlsx")

        os.startfile(path)
