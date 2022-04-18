#Modules;
import tkinter as tk
import os
import os, time
import datetime as dt
import shutil
from tkinter import *
from tkinter import filedialog as fd

class window(Frame): #frame has to be capitalized.
    def __init__(self,master):
        Frame.__init__(self) #frame has to be capitalized.

        self.master = master
        self.master.resizable(width = False, height = False) #fixed window dimension.
        self.master.geometry('{}x{}'.format(440,160)) #window size.
        self.master.title('File Transfer') #window title.
        self.master.config(bg = 'light gray') #window background color.

        self.inputOne = StringVar() #assigning a variable as a string by using the StringVar() method.
        self.inputTwo = StringVar() #assigning a variable as a string by using the StringVar() method.

    #Entry Widgets;
        #entry widget(first/top)
        self.inputOne = Entry(self.master, text=self.inputOne, width=41, font=("Helvetica", 10), fg='black', bg='white')
        self.inputOne.grid(row=0, column=1, columnspan=2, padx=(0,0), pady=(36,0))

        #entry widget(second/bottom)
        self.inputTwo = Entry(self.master, text=self.inputTwo, width=41, font=("Helvetica", 10), fg='black', bg='white')
        self.inputTwo.grid(row=1, column=1, columnspan=2, padx=(0,0), pady=(10,0))

    #Buttons;
        #source button.
        self.btnOpenOne = Button(self.master, text="Source:", width=12, height=1, command=self.usersSource)
        self.btnOpenOne.grid(row=0, column=0, padx=(15,16), pady=(36,0)) #(above) command calls child 'usersSource'.

        #destination button.
        self.btnOpenTwo = Button(self.master, text="Destination:", width=12, height=1, command=self.usersDestination)
        self.btnOpenTwo.grid(row=1, column=0, padx=(15,16), pady=(8,0)) #(above) command calls child 'usersDestination'.

        #transfer button.
        self.btnCheck = Button(self.master, text="Transfer Files", width=12, height=2, command=self.usersTransfer)
        self.btnCheck.grid(row=2, column=0, padx=(0,0), pady=(8,0)) #(above) command calls child 'usersTransfer'.

        #close button.
        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.usersClose)
        self.btnClose.grid(row=2, column=1, padx=(200,0), pady=(8,0)) #(above) command calls function 'usersClose'.

    def usersSource(self): #child function for 'source' button.
        folderName1 = fd.askdirectory() #'askdirectory' is for folders. for files, use 'askopenfilename'.
        self.inputOne.insert(0,folderName1) #Inserts users source path into the inputOne bar by using the insert() method)
        
    def usersDestination(self): #child function for 'destination' button.
        folderName2 = fd.askdirectory() #'askdirectory' is for folders. for files, use 'askopenfilename'.
        self.inputTwo.insert(0,folderName2) #Inserts users destination path into the inputTwo bar by using insert() method).

    def usersTransfer(self): #child function for 'transfer' button.
        sourcePath = self.inputOne.get() #retrieves users source folder path by using the get() method.
        destinationPath = self.inputTwo.get() #retrieves users destination folder path by using the get() method.
    #Date/Time;
        now = dt.datetime.now() #determines user current date/time.
        ago = now-dt.timedelta(hours=24) #determines user date/time within 24hrs.
        strftime = "%H:%m %m/%d/%Y" #hour:minute, month/day/year.
    #For Loop;
        for file_name in os.listdir(sourcePath):
            source = sourcePath
            destination = destinationPath
            if os.path.isfile(source):
                shutil.move(source,destination)
        
    def usersClose(self): #child function for 'close' button.
        self.master.destroy() #closes the window by using the destroy() method.

if __name__ == "__main__":
    root = Tk()
    App = window(root)


####The ".get" method grabs the text from an Entry widget, which 
####you can then save to a variable. Like this:
####
####sourcePath = self.inputOne.get()
####
####Your "transfer" function should also grab the destination path from the other Entry widget. That 
####Entry widget is named "self.inputTwo", so we'll use the ".get" method to retrieve the text from 
####it and save it to a variable, which we can name "destPath". Like this:
####
####destPath = self.inputTwo.get()
####
####Then, you would need to create a variable that holds the list of files in the source path, then 
####use a "for" loop to iterate through that list of files, and use "shutil.move" to move the files 
####from the source folder to the destination folder.

######Date/Time;
######        now = dt.datetime.now() #determines user current date/time.
######        ago = now-dt.timedelta(hours=24) #determines user date/time within 24hrs.
######        strftime = "%H:%m %m/%d/%Y" #hour:minute, month/day/year.
######    #For Loop;
######        for root, dirs,files in os.walk(sourcePath):
######            for x in files:
######                path = os.path.join(root,x)
######                st = os.stat(path)
######                mtime = dt.datetime.fromtimestamp(st.st_mtime)
######                if mtime > ago:
######                    shutil.move(sourcePath,destinationPath)
