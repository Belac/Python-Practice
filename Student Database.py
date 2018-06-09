print ("""
Student Database
\n
""")

import sqlite3

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

def AddStudent(conn,c,addStudent,studentFirst,studentLast,phoneNum):
    c.execute(addStudent%(studentFirst,studentLast,studentGender,phoneNum))
    conn.commit()

def AddClass(conn,c,addClass,customerID,productName):
    c.execute(addClass%(className,studentID))
    conn.commit()

def SelectAll(conn,c,Query_SelectAllCustomers,tableName):
    return c.execute(Query_SelectAllCustomers % tableName)

def Update(conn,c,UpdateStudent,tableName,studentForm,studentID):
    return c.execute(UpdateStudent % (tableName,studentForm,studentID))
    conn.commit()

#CreateStudentTable(conn,c,createStudentTable)
#CreateClassTable(conn,c,createClassTable)

x = 0
while x==0:
    cmd = input("What do you wish to do? (addstudent/addclass/showdatabase/changedata/exit): ")
    cmd = cmd.lower()
    if cmd == "addstudent":
        studentFirst = input("First Name: ")
        studentFirst = studentFirst.capitalize()
        studentLast = input("Last Name: ")
        studentLast = studentLast.capitalize()
        y = 0
        while y == 0:
            studentGender = input("Gender (M/F): ")
            studentGender = studentGender.upper()
            if studentGender == "M" or studentGender == "F":
                y = 1
            else:
                print ("INVALID GENDER \n")
        phoneNum = input("Phone Number: ")
        AddStudent(conn,c,addStudent,studentFirst,studentLast,phoneNum)
        print ("\n")
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

