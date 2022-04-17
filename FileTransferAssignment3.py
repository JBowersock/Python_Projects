#importing modules;
import tkinter as tk
import os, time
import datetime as dt
import shutil
from tkinter import *
from tkinter import filedialog as fd

#date/time
now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%m %m/%d/%Y"
source = '' #source path of Folder A.
destination = '' #destination path for Folder B.


for root, dirs,files in os.walk(source):
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            shutil.move(path,destination)

class window(Frame): #frame has to be capitalized.
    def __init__(self,master):
        Frame.__init__(self) #frame has to be capitalized.

        self.master = master
        self.master.resizable(width = False, height = False) #fixed window dimension.
        self.master.geometry('{}x{}'.format(440,160)) #window size.
        self.master.title('File Transfer') #window title.
        self.master.config(bg = 'light gray') #window background color.

        self.inputOne = StringVar()
        self.inputTwo = StringVar()

        #input text & grids #1(top)
        self.inputOne = Entry(self.master, text=self.inputOne, width=41, font=("Helvetica", 10), fg='black', bg='white')
        self.inputOne.grid(row=0, column=1, columnspan=2, padx=(0,0), pady=(36,0))

        #input text & grids #2(bottom)
        self.inputTwo = Entry(self.master, text=self.inputTwo, width=41, font=("Helvetica", 10), fg='black', bg='white')
        self.inputTwo.grid(row=1, column=1, columnspan=2, padx=(0,0), pady=(10,0))

        #browse button #1(top).
        self.btnOpenOne = Button(self.master, text="Source:", width=12, height=1, command=self.open) #command is action.
        self.btnOpenOne.grid(row=0, column=0, padx=(15,16), pady=(36,0)) #sticky tells the buttom where to stay.

        #browse button #2(bottom).
        self.btnOpenTwo = Button(self.master, text="Destination:", width=12, height=1, command=self.open2) #command is action.
        self.btnOpenTwo.grid(row=1, column=0, padx=(15,16), pady=(8,0)) #sticky tells the buttom where to stay.

        #transfer files button.
        self.btnCheck = Button(self.master, text="Transfer Files", width=12, height=2, command=self.transfer) #command is action.
        self.btnCheck.grid(row=2, column=0, padx=(0,0), pady=(8,0)) #sticky tells the buttom where to stay.

        #close program button.
        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.close) #command is action.
        self.btnClose.grid(row=2, column=1, padx=(200,0), pady=(8,0)) #sticky tells the buttom where to stay.

    def open(self):
        folderName = fd.askdirectory() #'askdirectory' is for folders. for files, use 'askopenfilename'.
        self.inputOne.insert(0,folderName) #INSERTs source path into the inputOne bar (using insert() method).

    def open2(self):
        folderName = fd.askdirectory() #'askdirectory' is for folders. for files, use 'askopenfilename'.
        self.inputTwo.insert(0,folderName) #INSERTs source path into the inputTwo bar (using insert() method).

    def transfer(self):
        self.inputOne = f #assign value to a variable.
        f.get() #get data from 'f'.
        f.write(self.inputTwo) #write data from 'f' to inputTwo.
        f.close() #close function.
        
    def close(self):
        self.master.destroy() #destroy closes the window.

if __name__ == "__main__":
    root = Tk()
    App = window(root)
