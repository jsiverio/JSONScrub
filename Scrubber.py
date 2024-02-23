import ujson as json
import re
import os
from tqdm import tqdm

class Scrubber:
     
    _IDENTIFIER = r"\bVICSDATAMODEL\b"  # VICS data model identifier
    _PDNAVALUE = "AAMANwABAD0AAQA9HgEBQ5oAFlFMAA0dAwYXcQMHDYcZBg2GUgotfcYAabpdABVPIyn/Gg1S/ylWTehHakHuaW8M5bjTBkV5JhNqAAZMnQBATLwDOX1fLEAgRG1SEzheHAQgAAMtNQgFYTU0DYpHKG0feShzBnwMBgMNAwEnFwkGM1gJGSqhATQUsANJDUwD" # PhotoDNA hash value to be removed

    
    def __init__(self, jsonSourcePath):
        self.jsonSourcePath = jsonSourcePath
        self.path = os.path.dirname(jsonSourcePath)
        self.fileName = os.path.basename(jsonSourcePath)
        self.dataModel = ""
    
    def _openJson(self):
        try:
            f = open(self.jsonSourcePath, "r")
        except OSError as e:
            print(e.strerror)
            exit(1)  
            
        data = json.load(f)
        f.close()
        self.dataModel = data['@odata.context'] 
        try:    
            if re.search(self._IDENTIFIER, self.dataModel): # Check if the JSON file is a VICS data model
                return data
            else:
                raise Exception("Invalid JSON file")
        except Exception as err:
            print(str(err))
            exit(1)
    
       
    def scrub(self):
        data = self._openJson()
        fileCount= len(data['value'][0]['Media'])
        
        self._fileInfo(data, fileCount)
        
        photoDNAFileCount = self._scanForPhotoDNA(data, fileCount)
        print("PhotoDNA File Found: " + str(photoDNAFileCount))
        
        if photoDNAFileCount > 0:
            print("\nRemoving PhotoDNA hash from VICS JSON File...")
            for i in tqdm (range(fileCount),"Scrubbing PhotoDNA hash..."):
                del data['value'][0]['Media'][i]['AlternativeHashes'][0]['HashName']
                del data['value'][0]['Media'][i]['AlternativeHashes'][0]['HashValue']
           
        dataOut = json.dumps(data, indent=2)
        newFileName = self.fileName.replace(".json", "_scrubbed.json")
        
        try:
            f = open(os.path.join(self.path,newFileName), "w")
            f.write(dataOut)
            f.close()
        except OSError as e:
            print(e.strerror)
            exit(1)
    
    def _fileInfo(self, data,fileCount):
        app = data['value'][0]['SourceApplicationName']
        paVersion = data['value'][0]['SourceApplicationVersion']
        
        print("\nPA VICS JSON Scrubber")
        print("JSON File Details")
        print("-----------------")
        print("File Name: " + self.fileName)
        print("File Count: " + str(fileCount))
        print("PA Version: " + app + " " + paVersion)
    
    def _scanForPhotoDNA(self, data, fileCount):
        pDNAFileCount = 0
        for i in tqdm (range(fileCount),"Scanning for PhotoDNA hash..."):
            if data['value'][0]['Media'][i]['AlternativeHashes'][0]['HashValue'] == self._PDNAVALUE:
                pDNAFileCount += 1
        return pDNAFileCount


