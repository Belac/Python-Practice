import sqlite3
import os

#-------------------------------------SQL--------------------------------------#

PathToDB="UserInformation.db"
createUserTable = """
    CREATE TABLE tblUsers(
        userID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        group CHAR(1) NOT NULL,
)
"""

addUser = """
    INSERT INTO tblUsers(username,password,group)
    VALUES ('%s','%s','%s','%s')
"""

UpdateUser = """
    UPDATE '%s'
    SET  = '%s'
    WHERE userID = '%s'
"""

selectAll = "SELECT * FROM %s"

conn = sqlite3.connect(PathToDB)
c = conn.cursor()

def CreateUserTable(conn,c,createUserTable):
    c.execute(CreateUserTable)
    conn.commit()

def AddUser(conn,c,addUser,username,password,group,):
    c.execute(addUser%(username,password,group,))
    conn.commit()

def SelectAll(conn,c,Query_SelectAllCustomers,tableName):
    return c.execute(Query_SelectAllCustomers % tableName)

def Update(conn,c,UpdateUser,tableName,userID):
    return c.execute(UpdateUser % (tableName,userID))
    conn.commit()


if not os.path.exists('UserInformation.db'):
    CreateUserTable(conn,c,createUserTable)
