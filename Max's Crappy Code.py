import sqlite3
from tkinter import *
#---------------------------------------SQL---------------------------------------#


PathToDB = "StudentDB.db"
Create_StudentTable = """
    CREATE TABLE tbl_Students(
        StudentNbr INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        StFname VARCHAR(20) NOT NULL,
        StSname VARCHAR(20) NOT NULL,
        StGender CHAR(1) NOT NULL,
        StForm VARCHAR(4) NOT NULL
)
"""

Create_ClassTable = """
    CREATE TABLE tbl_class(
        ClassNo INTEGER NOT NULL,
        ClassName VARCHAR(10) NOT NULL,
        StNbr INTEGER NOT NULL
)
"""

Add_Students = """
INSERT INTO tbl_Students(StFname,StSname,StGender,StForm)
VALUES('%s','%s','%s','%s')
"""

Add_Classes = """
INSERT INTO tbl_class(ClassNo,ClassName,StNbr)
VALUES('%s','%s','%s')
"""

Update_Students = """
UPDATE tbl_Students
SET StSname = "Froggo"
WHERE StudentNbr = "4"
"""

Add_Keys = """
ALTER TABLE tbl_class
ADD StForm VARCHAR(4) NOT NULL
"""


Query_SelectAllStudents = "SELECT * FROM %s"

conn = sqlite3.connect(PathToDB) 
c = conn.cursor()



#---------------------------------------Python---------------------------------------#


def createStudentTable(conn,c,Create_StudentTable):
    c.execute(Create_StudentTable)
    conn.commit()

def AddStudents(conn,c,Add_Students,StFname,StSname,StGender,StForm):
    c.execute(Add_Students%(StFname,StSname,StGender,StForm))
    conn.commit()

def createClassTable(conn,c,Create_ClassTable):
    c.execute(Create_ClassTable)
    conn.commit()

def AddClasses(conn,c,Add_Classes,ClassNo,ClassName,StNbr):
    c.execute(Add_Classes%(ClassNo,ClassName,StNbr))
    conn.commit()

def SelectAll(conn,c,Query_SelectAllStudents,tableName):
    return c.execute(Query_SelectAllStudents%tableName)

def UpdateSname(conn,c,Update_Students):
    c.execute(Update_Students)
    conn.commit()

def AddKeys(conn,c,Add_Keys):
    c.execute(Add_Keys)
    conn.commit()



createStudentTable(conn,c,Create_StudentTable)
UpdateSname(conn,c,Update_Students)
#createClassTable(conn,c,Create_ClassTable)

#StFname = input("Enter Student first name: ")
#StSname = input("Enter Student second name: ")
#StGender = input("Enter Student gender: ")
#StForm = input("Enter Student form: ")

#AddStudents(conn,c,Add_Students,StFname,StSname,StGender,StForm)

#ClassNo = input("Enter the class number: ")
#ClassName = input("Enter the class name: ")
#StNbr = input("Enter the student number: ")

#AddClasses(conn,c,Add_Classes,ClassNo,ClassName,StNbr)

#for rows in SelectAll(conn,c,Query_SelectAllStudents,"tbl_Students"):
    #print(rows)

#for rows in SelectAll(conn,c,Query_SelectAllStudents,"tbl_class"):
    #print(rows)


#---------------------------------------TKinter---------------------------------------#
root = Tk()

x = Entry(root)
y = Entry(root)
z = Entry(root)
w = Entry(root)
StFname = Entry(root)
StSname = Entry(root)
StGender = Entry(root)
StForm = Entry(root)

def save_student():
    StFname = x.get()
    StSname = y.get()
    StGender = z.get()
    StForm = w.get()
    AddStudents(conn,c,Add_Students,StFname,StSname,StGender,StForm)

Label(text='Student Forename:').pack(side=TOP,padx=10,pady=10)
x = str(Entry(root, width=20).pack(side=TOP,padx=10,pady=10))
Label(text='Student Surname:').pack(side=TOP,padx=10,pady=10)
y = str(Entry(root, width=20).pack(side=TOP,padx=10,pady=10))
Label(text='Gender:').pack(side=TOP,padx=10,pady=10)
z = str(Entry(root, width=20).pack(side=TOP,padx=10,pady=10))
Label(text='Form:').pack(side=TOP,padx=10,pady=10)
w = str(Entry(root, width=20).pack(side=TOP,padx=10,pady=10))
Button = Button(text="ENTER", command = save_student).pack(side = BOTTOM)
root.geometry("200x345")
root.mainloop()

for rows in SelectAll(conn,c,Query_SelectAllStudents,"tbl_Students"):
    print(rows)
