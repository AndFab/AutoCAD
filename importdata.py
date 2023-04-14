import openpyxl
import os

 # take the first sheet of the excel file at the source path.
def ImportData(source_path):
    if os.path.isfile(source_path):
        workbook = openpyxl.load_workbook(source_path)
        ws=[]
        for sheet in workbook:
            ws.append(sheet)
        return ws
    else:
        print("File does not exist at source path.")