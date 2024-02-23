## VICS JSON File Scrubber

About
---
The VICS JSON File Scrubber is a python script designed to remove the PhotoDNA hash value that is populated by Cellebrite Physical Analyzer when creating a VICS JSON export. It is important to note that Physical Analyzer does not compute the PhotoDNA hash value, and the hash being populated is the same for every property in the JSON file.

By running the script, you can easily remove the hash value from the JSON file, ensuring that it does not create problems when uploading to the ProjectVIC database.

Usage
---
`PDNAScrubber.py  path\to\your\VICS.json`  
To run the script, enter the path and filename of the JSON file and press enter. The script will generate a new file that is scrubbed of all PhotoDNA.



