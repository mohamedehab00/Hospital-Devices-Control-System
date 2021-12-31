import pandas as pd
import os
from LogOperations import createLogFile

Main_DB_Folder_Name = ".\\ExcelFiles\\"
Main_DB_File_Name = "DeviceDB"

DB_Cols = ["DeviceName", "ModelType", "Department", "FloorNo", "Manufacture", "Agent", "SerialNo", \
           "WarrantyPeriod", "InstallationDate", "PPM", "ppmPeriod", "firstPPM", "secondPPM", "thirdPPM", "fourthPPM"]


def check_Exist(File_Name):
    return os.path.isfile(Main_DB_Folder_Name + File_Name + ".xlsx")


def checkSerialExist(serial):
    try:
        df = pd.read_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx", dtype={"SerialNo": str})
        cond = df["SerialNo"] == serial
        result = df[cond].index
        res = len(result)
        print(res, " ", result)
        if res > 0:
            return [False, result]
        else:
            return [True, -1]
    except:
        return [True, -1]


def check_no_duplicated_serial(serial):
    if not check_Exist(Main_DB_File_Name):
        return True
    else:
        return checkSerialExist(serial)[0]


def insertRecord(data):
    if not check_Exist(Main_DB_File_Name):
        df = pd.DataFrame(data={"DeviceName": [], "ModelType": [], "Department": [], "FloorNo": [], "Manufacture": [], \
                                "Agent": [], "SerialNo": [], "WarrantyPeriod": [], "InstallationDate": []
            , "PPM": [], "ppmPeriod": [], "firstPPM": [], "secondPPM": [], "thirdPPM": [], "fourthPPM": []},
                          columns=DB_Cols)
        df = df.append(data, ignore_index=True)
        df.to_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx", encoding="utf-8", index=False)
    else:
        df = pd.read_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx")
        df.reset_index(drop=True, inplace=True)
        df = df.append(data, ignore_index=True)
        df.to_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx", encoding="utf-8", index=False)
    createLogFile(data)


def deleteRecord(serial):
    if check_Exist(Main_DB_File_Name):
        df = pd.read_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx")
        df.reset_index(drop=True, inplace=True)
        idx = df[df["SerialNo"] == serial].index
        df.drop(idx, inplace=True)
        df.to_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx", encoding="utf-8", index=False)


def searchRecord(serial):
    if check_Exist(Main_DB_File_Name):
        Exist = checkSerialExist(serial)
        print(Exist)
        ExistCond, ExistIdx = Exist[0], Exist[1]
        if ExistCond:
            return [False, {"DeviceName": "NOT FOUND", "ModelType": "NOT FOUND", "Department": "NOT FOUND",
                            "FloorNo": "NOT FOUND", "Manufacture": "NOT FOUND", "Agent": "NOT FOUND",
                            "SerialNo": "NOT FOUND", \
                            "WarrantyPeriod": "NOT FOUND", "InstallationDate": "NOT FOUND", "PPM": "NOT FOUND",
                            "ppmPeriod": "NOT FOUND", "firstPPM": "NOT FOUND", "secondPPM": "NOT FOUND",
                            "thirdPPM": "NOT FOUND",
                            "fourthPPM": "NOT FOUND"}]
        else:
            df = pd.read_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx")
            df.reset_index(drop=True, inplace=True)
            data = {}
            for i in range(len(DB_Cols)):
                data[DB_Cols[i]] = df.at[ExistIdx.values[0], DB_Cols[i]]
            print(data)
            return [True, data]
    else:
        return [False, {"DeviceName": "NOT FOUND", "ModelType": "NOT FOUND", "Department": "NOT FOUND",
                        "FloorNo": "NOT FOUND", "Manufacture": "NOT FOUND", "Agent": "NOT FOUND",
                        "SerialNo": "NOT FOUND", \
                        "WarrantyPeriod": "NOT FOUND", "InstallationDate": "NOT FOUND", "PPM": "NOT FOUND",
                        "ppmPeriod": "NOT FOUND", "firstPPM": "NOT FOUND", "secondPPM": "NOT FOUND",
                        "thirdPPM": "NOT FOUND",
                        "fourthPPM": "NOT FOUND"}]


def getUpcoming(month):
    if not check_Exist(Main_DB_File_Name):
        return (False, [])
    else:
        data = []
        df = pd.read_excel(Main_DB_Folder_Name + Main_DB_File_Name + ".xlsx")
        cond = (df["firstPPM"] == month) | (df["secondPPM"] == month) | (df["thirdPPM"] == month) | (
                    df["fourthPPM"] == month)
        df = df[cond]
        for index, row in df.iterrows():
            rows = {}
            rows["DeviceName"] = "Device : " + str(row["DeviceName"])
            rows["ModelType"] = "Model : " + str(row["ModelType"])
            rows["SerialNo"] = "S.N : " + str(row["SerialNo"])
            rows["Department"] = "Depart. : " + str(row["Department"])
            rows["FloorNo"] = "Floor : " + str(row["FloorNo"])
            rows["firstPPM"] = "1st PPM : " + str(row["firstPPM"])
            rows["secondPPM"] = "2nd PPM : " + str(row["secondPPM"])
            rows["thirdPPM"] = "3rd PPM : " + str(row["thirdPPM"])
            rows["fourthPPM"] = "4th PPM : " + str(row["fourthPPM"])
            data.append(rows)
        return (True, data)
