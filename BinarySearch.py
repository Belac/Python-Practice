#BinarySearch

sortedList = [1,2,2,3,3,3,4,5,5,5,6,6,8,9,9]
try:
    userSearch = int(input("What number do you wish to search for? "))
except:
    print ("Please enter a number.")

def BinarySearch(sortedList):
    n = len(sortedList)
    halfn = (n/2)
    halfn = int(halfn)

    if sortedList[halfn] == userSearch:
        print (halfn)
    elif userSearch > halfn:
        sortedList.remove[halfn:]
    elif userSearch < halfn:
        sortedList.remove[:halfn]
        BinarySearch(sortedList)
        return sortedList
    else:
        print ("I think there's been a bit of an error.")

BinarySearch(sortedList)
print(sortedList)
