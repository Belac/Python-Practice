print("""
Data Collection Software
""")

import sqlite3

PathToDB= "CustomerDB.db"
Create_CustomerTable="""
    CREATE TABLE tbl_Customer(
        customerID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        customerTitle VARCHAR(4) NOT NULL,
        customerFirstName VARCHAR(32) NOT NULL,
        customerLastName VARCHAR(32) NOT NULL,
        customerPhoneNo UNSIGNED INTEGER(11) NOT NULL
    )
"""

Create_TransactionTable="""
    CREATE TABLE tbl_Transaction(
        receiptID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        customerID INTEGER NO NULL,
        productName VARCHAR(50) NOT NULL
    )
"""

Add_Customers = """
    INSERT INTO tbl_Customer(customerTitle,customerFirstName,customerLastName,customerPhoneNo)
    VALUES('%s','%s','%s','%s')
"""

Add_Products = """
    INSERT INTO tbl_Transaction(customerID,productName)
    VALUES('%s','%s')
"""

Query_SelectAllCustomers = "SELECT * FROM %s" #Selects all rows in the DB
Query_CustomerTitle = """
    SELECT * FROM tbl_Customer WHERE
        customerTitle = "Sir"
"""

conn = sqlite3.connect(PathToDB) #Creates a connection to the database
c = conn.cursor() #Creates a container for the commands being sent to the database.

def CreateCustomerTable(conn,c,Create_CustomerTable):
    c.execute(Create_CustomerTable)
    conn.commit()

def CreateTransactionTable (conn,c,Create_TransactionTable):
    c.execute(Create_TransactionTable)
    conn.commit()

def AddCustomer(conn,c,Add_Customers,title,firstName,lastName,phoneNum):
    c.execute(Add_Customers%(title,firstName,lastName,phoneNum))
    conn.commit()

def AddProduct(conn,c,Add_Products,customerID,productName):
    c.execute(Add_Products%(customerID,productName))
    conn.commit()

def SelectAll(conn,c,Query_SelectAllCustomers,tableName):
    return c.execute(Query_SelectAllCustomers % tableName)

def QueryTitle(conn,c,Query_CustomerTitle):
    return c.execute(Query_CustomerTitle)

#CreateCustomerTable(conn,c,Create_CustomerTable) #CreateCustomerTable(conn,c,Create_CustomerTable)
#CreateTransactionTable(conn,c,Create_TransactionTable)
x=0
while x == 0:
    cmd = input("What do you wish to do? (newuser/addtrans/showdatabase/exit): ")
    cmd = cmd.lower()
    if cmd == "newuser":
        title = input("Please enter your title (Mr/Ms): ")
        firstName = input("First Name: ")
        firstName = firstName.capitalize()
        initial = firstName[0]
        lastName = input("Last Name: ")
        lastName = lastName.capitalize()
        phoneNum = input("Phone Number: ")
        AddCustomer(conn,c,Add_Customers,title,firstName,lastName,phoneNum)
        print ("\n")
    elif cmd == "addtrans":
        customerID = input("Customer's ID: ")
        productName = input("Product Name: ")
        AddProduct(conn,c,Add_Products,customerID,productName)
        print ("\n")
    elif cmd == "showdatabase":
        print ("\n")
        print ("ID, Title, First Name, Last Name, Phone Number")
        for rows in SelectAll(conn,c,Query_SelectAllCustomers,"tbl_Customer"):
            print(rows)
        print ("\n\n")
        print ("Transaction ID, Customer ID, Product Name")
        for rows in SelectAll(conn,c,Query_SelectAllCustomers,"tbl_Transaction"):
            print(rows)
        print ("\n")
    elif cmd == "exit":
        x = 1
    else:
        print ("Unfortunately, you can't do that.")
        print ("\n")

