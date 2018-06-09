"""
Linked Lists
Author: J Hood
Date: 23 May 2018
"""
Register = [["Hood",5],["Allan",2],["Bennett",0],["Todd",4],["Yale","null"],["Merton",3]]
Start = 1
NextFree = 6

#write a procedure to printout the above linked list in the correct order
def SortList(list):
    print (sorted(list))
print(SortList(Register))

def SortListManual(list):
    print("Register Ordered Alphabetially Ascending")
    p = (list[Start][1])
    print ("Pointer Position: ",p)
    while p != "null":
        print(list[p][0])
        p = list[p][1]
        print ("Pointer Position: ",p)
SortListManual(Register)

#Extra challenge - write a procedure to add "Johnson" to the above list and update
def AddToList(list,entry):
    entry = input("What would you like to add?")
    entry = [input,]
    list.append(entry)

#the pointers
