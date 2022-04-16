import os, time
import datetime as dt
import shutil

#implementing the current time and date.
now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%m %m/%d/%Y"
source = 'C:/Users/Streaming Desktop/Desktop/A/' #source path of Folder A.
destination = 'C:/Users/Streaming Desktop/Desktop/B/' #destination path for Folder B.

for root, dirs,files in os.walk(source):
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            shutil.move(path,destination)

#note: by running the this file at this point, it will transfer the files.

#-------------------------------------
##FILE TRANSFER PART TWO ASSIGNMENT (Python Step 316)
##
##But now your company's users create or edit a collection of text files throughout the day.
##These text files represent data about customer orders.
##
##Once per day, any files that are new, or that were edited within the previous 24 hours, must
##be sent to the home office. To facilitate this, these new or updated files need to be copied
##to a specific 'destination' folder on a computer so that a special file transfer program can
##grab them and transfer them to the home office.
##
##The process of figuring out which files are new or recently edited (and copying them to the
##'destination' folder), is currently being done manually. This is very expensive in terms of
##manpower.
##
##Create two folders: one to hold the files that get created or modified throughout the day,
##and another to receive the files that your script determines should be copied over daily.
##
##To aid in your development efforts, you should create .txt files to add to the first folder,
##using Notepad or a similar program. You should also copy some older text files in there if
##you'd like. You should use files that you can edit so that you can control whether or not
##they are meant to be detected as 'modified in the last 24 hours' by your program.
##
##Create a script that will automate this task.
