import os #importing operating system.

def writeData(): #created function which opens a file, writes data within it and prints it.
    data = '\nHello World!' #the data being entered into the file.
    with open('text.docx', 'a') as f: #saying while text.docx is open, to Append it with 'a' and call that file 'f' with 'as'.
        f.write(data) #writes the data to the file.
        f.close() #closing the file.

def openFile(): #created function which opens a file, reads data and prints it.
    with open('text.docx', 'r') as f: #saying while text.docx is open, to Read it with 'r' and call that file 'f' with 'as'.
        data = f.read() #read 'f', submit that information into variable called 'data'.
        print(data) #print data to idle shell.
        f.close() #closing the file.

if __name__ == "__main__":
    writeData()
    openFile()
