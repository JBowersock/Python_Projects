import tkinter
from tkinter import *

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
        self.btnOpenTwo = Button(self.master, text="Browse...", width=12, height=1, command=self.open) #command is action.
        self.btnOpenTwo.grid(row=1, column=0, padx=(15,16), pady=(8,0)) #sticky tells the buttom where to stay.

        #check files button.
        self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2, command=self.open) #command is action.
        self.btnCheck.grid(row=2, column=0, padx=(0,0), pady=(8,0)) #sticky tells the buttom where to stay.

        #close program button.
        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.close) #command is action.
        self.btnClose.grid(row=2, column=1, padx=(200,0), pady=(8,0)) #sticky tells the buttom where to stay.

    def open(self):
        self.lblDisplay.config(text=''.format(fn,ln))
        #config is used to change something dynamically in the middle of a runnng program.

    def close(self):
        self.master.destroy() #destroy closes the window.

if __name__ == "__main__":
    root = Tk()
    App = window(root)
    root.mainloop() #if we dont do this, it wont continuously run.
