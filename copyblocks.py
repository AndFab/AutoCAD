from pyautocad import APoint
import os

def CopyBlocks(source_path, modelspace, document):
    if os.path.isfile(source_path):
        block = modelspace.AttachExternalReference(source_path, "Ref", APoint(0,0,0), 1,1,1,0, False)
        document.Blocks.Item(block.Name).Bind(True)
        block.Delete()
    else:
        print("File does not exist at source path.")
    
