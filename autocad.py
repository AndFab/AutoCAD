from pyautocad import Autocad, APoint
import openpyxl
from copyblocks import CopyBlocks
from importdata import ImportData


 # Create a connection to the running instance of AutoCAD
acad = Autocad()

 # Retrieve the currently active document in AutoCAD application and assign it to acadDoc
acadDoc = acad.ActiveDocument
print(f"The open DWG file is: {acadDoc.Name}")

 # Retrieve the "ModelSpace" object of the currently active AutoCAD document and assign it to acadModel
acadModel = acad.model

 # Run function "CopyBlocks" to import blocks from file at the source path
source_path = r"" + input("Enter the full source path to blocks into current document: ")
CopyBlocks(source_path, acadModel, acadDoc)

 # Run function "ImportData" to import datasheets from excel file at the source path
datasource_path = r"" + input("Enter the full source path to the data file: ")
data_sheet = ImportData(datasource_path)
