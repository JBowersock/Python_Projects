import tkinter as tk
from tkinter import *

class window(Frame): #frame has to be capitalized.
    def __init__(self,master):
        Frame.__init__(self) #frame has to be capitalized.

        self.master = master
        self.master.resizable(width = False, height = False) #fixed window dimension.
        self.master.geometry('{}x{}'.format(440,160)) #window size.
        self.master.title('Check files') #window title.
        self.master.config(bg = 'light gray') #window background color.

        self.varFName = StringVar()
        self.varLName = StringVar()

        #input text & grids.
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 10), fg='black', bg='white')
        self.txtFName.grid(row=0, column=1, columnspan=2, padx=(0,0), pady=(36,0))

        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 10), fg='black', bg='white')
        self.txtLName.grid(row=1, column=1, columnspan=2, padx=(0,0), pady=(10,0))

        #browse1 button.
        self.btnOpen = Button(self.master, text="Browse...", width=12, height=1, command=self.open) #command is action.
        self.btnOpen.grid(row=0, column=0, padx=(15,0), pady=(36,0)) #sticky tells the buttom where to stay.

        #browse2 button.
        self.btnOpen = Button(self.master, text="Browse...", width=12, height=1, command=self.open) #command is action.
        self.btnOpen.grid(row=1, column=0, padx=(15,0), pady=(8,0)) #sticky tells the buttom where to stay.

        #checkfile button.
        self.btnOpen = Button(self.master, text="Check for files...", width=12, height=2, command=self.open) #command is action.
        self.btnOpen.grid(row=2, column=0, padx=(15,0), pady=(8,0)) #sticky tells the buttom where to stay.

        #close button.
        self.btnSubmit = Button(self.master, text="Close Program", width=12, height=2, command=self.close) #command is action.
        self.btnSubmit.grid(row=2, column=1, padx=(225,0), pady=(8,0)) #sticky tells the buttom where to stay.

    def open(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text=''.format(fn,ln))
        #config is used to change something dynamically in the middle of a runnng program.

    def close(self):
        self.master.destroy() #destroy closes the window.

if __name__ == "__main__":
    root = Tk()
    App = window(root)
    root.mainloop() #if we dont do this, it wont continuously run.
