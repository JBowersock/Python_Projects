import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd

class window(Frame): #frame has to be capitalized.
    def __init__(self,master):
        Frame.__init__(self) #frame has to be capitalized.

        self.master = master
        self.master.resizable(width = False, height = False) #fixed window dimension.
        self.master.geometry('{}x{}'.format(440,160)) #window size.
        self.master.title('Check files') #window title.
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
        self.btnOpenOne = Button(self.master, text="Browse...", width=12, height=1, command=self.open) #command is action.
        self.btnOpenOne.grid(row=0, column=0, padx=(15,16), pady=(36,0)) #sticky tells the buttom where to stay.

        #browse button #2(bottom).
        self.btnOpenTwo = Button(self.master, text="Browse...", width=12, height=1, command=self.open2) #command is action.
        self.btnOpenTwo.grid(row=1, column=0, padx=(15,16), pady=(8,0)) #sticky tells the buttom where to stay.

        #check files button.
        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2, command=self.open) #command is action.
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
        
    def close(self):
        self.master.destroy() #destroy closes the window.

if __name__ == "__main__":
    root = Tk()
    App = window(root)

#------------------------------------------
##WIDGET CHALLENGE (Python Step 309)
##
##For this assignment, you will write a script that creates a GUI with a button widget and a text widget.
##We recommend using the GUI from the previous assignment, though this is not required. Your script will
##also include a function that, when it is called, will invoke a dialog modal which will allow users the
##ability to select a folder directory from their system. Finally, your script will show the user’s selected
##directory path in the text field.
##
##REQUIREMENTS:
##Your script will need to use Python 3 and the Tkinter module.
##
##Your script will need to use the askdirectory( ) method from the Tkinter module.
##
##Your script will need to have a function linked to the button widget so that once the button has been clicked,
##the user’s selected file path will be retained by the askdirectory( ) method and printed within your GUI’s text widget.
