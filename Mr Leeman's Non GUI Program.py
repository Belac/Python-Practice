import csv
from AccountLogin import *

while loginx == True:
    use = input("Enter the username: ")
    pas = input("Enter the password: ")
    usercheck(use,pas)

print ("\n\n")

with open("children.txt","w") as csvfile:
    options = input("What do you wish to do? (Input Student Data / Read Child File)")
    options = options.upper()
    if options == "INPUT STUDENT DATA":
        childphile = csv.writer(csvfile, delimiter=',')
        childforename = input("Child First Name: ")
        childsurname = input("Child Surname: ")
        childdob = input("Child DOB: ")
        childhome = input("Child Home Address: ")
        childhomeno = input("Child Home Phone Number: ")
        childgender = input("Child Gender: ")
        childtutor = input("Child Tutor Group: ")
        childschoolemail = input("Child School Email Address: ")
        childdata = (childforename,childsurname,childdob,childhome,childhomeno,childgender,childtutor,childschoolemail)
        childphile.writerow(childdata)
    if options == "READ CHILD FILE":
        childphile = csv.reader(csvfile, delimiter=',')
        for row in childphile:
            print (row)
    else:
        print ("ERROR, WRITE SOMETHING VALID PLEASE")

