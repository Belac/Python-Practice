myString = input("Please enter a word or phrase: ")
list1 = []
list2 = []
numChars = len(list1)
n = 0

for i in myString:
    list1.append(i)
for i in reversed(myString):
    list2.append(i)

if list1 == list2:
    print ("It is a palendrome.")
else:
    print ("It is not a palendrome.")