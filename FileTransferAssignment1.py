import os
import shutil

#set the source path of Folder A.
source = 'C:/Users/Streaming Desktop/Desktop/A/'

#set the destination path for Folder B.
destination = 'C:/Users/Streaming Desktop/Desktop/B/'
files = os.listdir(source)

for i in files:
    #we are saying to move the files represented by 'i' to their new destination.
    shutil.move(source+i, destination)

#note: by running the this file at this point, it will transfer the files.

#-------------------------------------
##FILE TRANSFER PART ONE ASSIGNMENT (Python Step 315)
##
##NOTE: This is a three-part assignment. Ensure to save all your code files for this
##assignment because you will be uploading them to GitHub for review by an Instructor.
##
##Your employer wants a program to move all their text files (with a .txt file extension)
##from one folder to another with the click of a button. On your desktop you will have
##two new folders, one called Folder A and another called Folder B. You will need to move
##text files from Folder A to Folder B.
##
##Complete the following steps:
##
##Create two new folders on your desktop labeled Folder A and Folder B.
##
##Create four .txt files, each with some meaningless content such as “this is file 1”
##etc., in Folder A.
