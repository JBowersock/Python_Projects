import os

fName = 'text.docx'

fPath = 'C:\\TTA_Python_Projects\\' #The reason there are 2 \'s back to back, is so Python will ignore the error.

abPath = os.path.join(fPath,fName)
print(abPath)
