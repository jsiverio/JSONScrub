import ujson as json
import re

class Scrubber:
    _IDENTIFIER = r"\bVICSDATAMODEL\b"
    _PDNAVALUE = "AAMANwABAD0AAQA9HgEBQ5oAFlFMAA0dAwYXcQMHDYcZBg2GUgotfcYAabpdABVPIyn/Gg1S/ylWTehHakHuaW8M5bjTBkV5JhNqAAZMnQBATLwDOX1fLEAgRG1SEzheHAQgAAMtNQgFYTU0DYpHKG0feShzBnwMBgMNAwEnFwkGM1gJGSqhATQUsANJDUwD"

   

    def __init__(self, jsonSourcePath):
        self.jsonSourcePath = jsonSourcePath
        self.dataModel = ""
    
    def _openJson(self):
        try:
            f = open(self.jsonSourcePath, "r")
            data = json.load(f)
            self.dataModel = data['@odata.context']
            if re.search(self._IDENTIFIER, self.dataModel):    
                return data
        except: 
            return None
    
    
    def check(self):
        data = self._openJson()
        fileCount= len(data['value'][0]['Media'])
        for i in range(fileCount):
            pDnaIdentifier = data['value'][0]['Media'][i]['AlternativeHashes'][0]['HashName']
            pDnaHashValue = data['value'][0]['Media'][i]['AlternativeHashes'][0]['HashValue']
            if pDnaIdentifier == 'PhotoDNA' and pDnaHashValue == self._PDNAVALUE:
                pDnaIdentifier= ""                
                pDnaHashValue= ""
    
            
        
    


# Keys '@odata.context' and 'value'

scrubber = Scrubber("51001484536.json")
dat = scrubber.check()
