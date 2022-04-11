import sqlite3

conn = sqlite3.connect('assignment.db') #connecting to the database, which we're creating right here.

#creating the new table.
with conn: #with means while 'conn' is open.
    cur = conn.cursor() #cur is just a short name we gave for cursor. cursor operates the database when commands are given.
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filenames( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename STRING \
        )")
    conn.commit() #commiting conn to database.
conn.close() #closing conn from database.

conn = sqlite3.connect('assignment.db') #we closed the connection above, so here we are opening a new one.

#tuple of files
files_tuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in files_tuple: #for loop, goes through all values in 'file_tuple'.
    if x.endswith('.txt'): #if condition with 'endswith' parameters.
        with conn: #with means while 'conn' is open.
            cur = conn.cursor() #cur is just a short name we gave for cursor. cursor operates the database when commands are given.
            cur.execute("INSERT INTO tbl_filenames (col_filename) VALUES (?)", (x,))
            print(x) #prints x to IDLE Shell.
conn.close() #closing conn from database.


##DATABASE SUBMISSION ASSIGNMENT
##
##For this assignment, you will need to write a script that creates a database and adds new data into that
##database.
##
##
##REQUIREMENTS:
##
##Your script will need to use Python 3 and the sqlite3 module.
##
##Your database will require 2 fields: an auto-increment primary integer field and a field with the data type
##“string.”
##
##Your script will need to read from the supplied list of file names at the bottom of this page and determine
##only the files from the list which end with a “.txt” file extension.
##
##Next, your script should add those file names from the list ending with “.txt” file extension within your
##database.
##
##Finally, your script should legibly print the qualifying text files to the console.
##
##Add comments throughout your Python explaining your code. Adding comments to your code is a good practice,
##and is expected in the industry. It will help you understand what your code is doing and will also make it
##easier when you need reference back to previous projects.
##
##
##SETUP INSTRUCTIONS:
##
##The following is the list of file names to use for this assignment:
##information.docx, Hello.txt, myImage.png, myMovie.mpg, World.txt, data.pdf, myPhoto.jpg.
