
import sqlite3
from tkinter import *
import Userslib

#-------------------------------------SQL--------------------------------------#

PathToDB="StudentDB.db"
createStudentTable = """
    CREATE TABLE tblStudent(
        studentID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        studentFirst VARCHAR(20) NOT NULL,
        studentLast VARCHAR(20) NOT NULL,
        studentGender CHAR(1) NOT NULL,
        studentForm VARCHAR(5) NOT NULL
)
"""
createClassTable = """
    CREATE TABLE tblClass(
        classID INTEGER AUTOINCREMENT NOT NULL,
        className VARCHAR(10) NOT NULL,
        studentID INTEGER NOT NULL
)
"""

addStudent = """
    INSERT INTO tblStudent(studentFirst,studentLast,studentGender,studentForm)
    VALUES ('%s','%s','%s','%s')
"""
addClass = """
    INSERT INTO tblClass(className,studentID)
    VALUES ('%s','%s')
"""
UpdateStudent = """
    UPDATE '%s'
    SET studentForm = '%s'
    WHERE studentID = '%s'
"""

selectAll = "SELECT * FROM %s"

conn = sqlite3.connect(PathToDB)
c = conn.cursor()

def CreateStudentTable(conn,c,createStudentTable):
    c.execute(createStudentTable)
    conn.commit()

def CreateClassTable (conn,c,createClassTable):
    c.execute(createClassTable)
    conn.commit()

def AddStudent(conn,c,addStudent,studentFirst,studentLast,studentGender,studentForm):
    c.execute(addStudent%(studentFirst,studentLast,studentGender,studentForm))
    conn.commit()

def AddClass(conn,c,addClass,customerID,productName):
    c.execute(addClass%(className,studentID))
    conn.commit()

def SelectAll(conn,c,Query_SelectAllCustomers,tableName):
    return c.execute(Query_SelectAllCustomers % tableName)

def Update(conn,c,UpdateStudent,tableName,studentForm,studentID):
    return c.execute(UpdateStudent % (tableName,studentForm,studentID))
    conn.commit()

#--------------------------------BACKGROUND------------------------------------#
registered = 0
User = ("")
Pass = ("")

def raise_frame(frame):
    frame.tkraise()

ui = Tk()
u0 = Frame(ui)
u1 = Frame(ui)
u2 = Frame(ui)

studentfirstentry = Entry(ui)
studentlastentry = Entry(ui)
studentgenentry = Entry(ui)
studformentry = Entry(ui)

studentFirst = Entry(ui)
studentLast = Entry(ui)
studentGender = Entry(ui)
studentForm = Entry(ui)

for frame in (u1, u2):
    frame.grid(row=0, column=0, sticky='news')

def addstudent():
    studentFirst = studfirstentry.get()
    studentFirst = studentFirst.capitalize()
    studentLast = studlastentry.get()
    studentLast = studentLast.capitalize()
    studentGender = studgenentry.get()
    studentGender = studentGender.upper()
    studentForm = studformentry.get()
    AddStudent(conn,c,addStudent,studentFirst,studentLast,studentGender,studentForm)
    print ("\n")

def showdata():
    print ("\n")
    print ("ID, Student Name, Last Name, Gender, Form")
    for rows in SelectAll(conn,c,selectAll,"tblStudent"):
        print(rows)
    print ("\n")

def register(newid,newpass):
    Userslib.AddUser(conn,c,createUserTable)
    User = newid.get()
    Pass = newpass.get()
    lambda:raise_frame(u1)

#CreateStudentTable(conn,c,createStudentTable)
#CreateClassTable(conn,c,createClassTable)

#-----------------------------------UI-----------------------------------------#

raise_frame(u0)
if registered == 0:
    u0.grid(row=0,column=0,sticky="nsew")
    usernamelabel = Label(u0,text="Username")
    usernamelabel.pack(pady=5,padx=50)
    newid = Entry(u0)
    newid.pack(pady=5)
    passwordlabel = Label(u0,text="Password")
    passwordlabel.pack(pady=5,padx=50)
    newpass = Entry(u0)
    newpass.pack(pady=5)
    registerbut = Button(u0,text="Register",command=register).pack()

ui.title("StudentDB")
maintitle = Label(u1, text="~~ The Student Database ~~")
maintitle.pack()
addstudentoption = Button(u1,text="Add Student",command=lambda:raise_frame(u2)).pack()

studfirst = Label(u2,text="First Name")
studfirst.pack(pady=5,padx=50)
studfirstentry = Entry(u2)
studfirstentry.pack(pady=5)
studlast = Label(u2,text="Last Name")
studlast.pack(pady=5)
studlastentry = Entry(u2)
studlastentry.pack(pady=5)
studgen = Label(u2,text="Gender")
studgen.pack(pady=5)
studgenentry = Entry(u2)
studgenentry.pack(pady=5)
studnum = Label(u2,text="Form")
studnum.pack(pady=5)
studformentry = Entry(u2)
studformentry.pack(pady=5)
add = Button(u2,text="Add Student",command=addstudent)
add.pack(pady=5)
showdata()

ui.mainloop()

#--------------------------------OTHER-----------------------------------------#
"""
cmd = input("What do you wish to do? (addstudent/addclass/showdatabase/changedata/exit): ")
cmd = cmd.lower()

elif cmd == "addclass":
    className = input("Class Name: ")
    studentID = input("Student ID: ")
    AddClass(conn,c,addClass,className,studentID)
    print ("\n")
elif cmd == "showdatabase":
    print ("\n")
    print ("ID, Student Name, Last Name")
    for rows in SelectAll(conn,c,selectAll,"tblStudent"):
        print(rows)
    print ("\n")
elif cmd == "changedata":
    studentID = input("Student ID: ")
    studentForm = input("Student Form: ")
    Update(conn,c,UpdateStudent,"tblStudent",studentForm,studentID)
elif cmd == "exit":
    x = 1
else:
    print ("Unfortunately, you can't do that.")
    print ("\n")
"""
