#Step 310;
function1 = open('WebPageGeneratorAssignment.html', 'a') #this creates a new file (using 'a'), in the same folder.

#import modules;
import webbrowser #importing module.
                        
url = 'WebPageGeneratorAssignment.html' #assigning value to a variable.
webbrowser.open(url,new=2) #opens new tab in browser with the file.

function1.write("Stay tuned for our amazing summer sale!") #write method.
function1.close() #close method.

#Step 311;
#import modules;
import tkinter
from tkinter import *

class window(Frame): #frame has to be capitalized.
    def __init__(self,master):
        Frame.__init__(self) #frame has to be capitalized.

        self.master = master
        self.master.resizable(width = False, height = False) #fixed window dimension.
        self.master.geometry('{}x{}'.format(800,300)) #window size.
        self.master.title('Write to Page') #window title.
        self.master.config(bg = 'light gray') #window background color.

        self.input = StringVar()

        #input text & grids #1(top)
        self.input = Entry(self.master, text=self.input, width=109, font=("Helvetica", 10), fg='black', bg='white')
        self.input.grid(row=0, column=0, columnspan=2, padx=(16,0), pady=(15,0), ipady=100) #ipady adjusts input height.

        #enter button #1(top).
        self.btnSubmit = Button(self.master, text="Submit", width=12, height=2, command=self.submit) #command is action.
        self.btnSubmit.grid(row=1, column=0, padx=(575,0), pady=(12,0), sticky=E) #sticky tells the buttom where to stay.

        #close program button.
        self.btnClose = Button(self.master, text="Close", width=12, height=2, command=self.close) #command is action.
        self.btnClose.grid(row=1, column=1, padx=(0,0), pady=(12,0), sticky=E) #sticky tells the buttom where to stay.

    def submit(self):
        userText = self.input.get() #GETs the text from the entry widget and saves it to a variable named 'userText'
        htmlCode = "<!DOCTYPE HTML><head></head><body>" + userText + "</body></html>" #creates a variable holding the HTML code.
        f = open ('WebPageGeneratorAssignment.html', 'w') #opens the HTML file in write mode.
        f.write(htmlCode) #writes the HTML code to the file.
        f.close()
        webbrowser.open_new_tab('WebPageGeneratorAssignment.html') #opens the HTML file in the browser.

    def close(self):
        self.master.destroy() #destroy closes the window.

if __name__ == "__main__":
    root = Tk()
    App = window(root)
    root.mainloop() #if we dont do this, it wont continuously run.

##----------------------------------------------------------------------------------------------------------------------
##WEB PAGE GENERATOR PART ONE ASSIGNMENT (Python Step 310)
##
##You’ve been asked by users for a tool that can automatically create a basic HTML web page.
##
##The page is very simple. It will simply have the text "Stay tuned for our amazing summersale!"
##on the page.
##
##Your task is to create a Python script that will automatically create the .html file needed.
##The file will be very simple. It will look like this:
##
##<html>
##    <body>
##        <h1>
##            Stay tuned for our amazing summer sale!
##        </h1>
##    </body>
##</html>
##
##The script should open this new html file in a new tab within your browser that displays:
##
##Stay tuned for our amazing summer sale!

##----------------------------------------------------------------------------------------------------------------------
##WEB PAGE GENERATOR PART TWO ASSIGNMENT (Python Step 311)
##
##Now that you have created a tool that can automatically create a basic HTML web page, the content on the
##page is hard-coded as "Stay tuned for our amazing summer sale!"
##
##Users have now asked you to create an option for them to set the body of the text themselves.
##
##Your task is to create a GUI with Tkinter that will enable the users to set the body text for a
##newly-created web page. There should also be a control in the GUI that initiates the process of making
##the new web page.
##
##Set a new body text of your choice.
##
##The GUI should open the html file in a new tab within your browser that displays the newly added text
##from the user.
