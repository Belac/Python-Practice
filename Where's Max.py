#findmax

numberlist = [34,89,87,23,1,43,56,32,4,5,77,44,54,23,31,230]

def maxInt(listInt):
    maxNumber = listInt[0]
    for i in range(1,(len(listInt))):
        if listInt[i] > maxNumber:
            maxNumber = listInt[i]
    return maxNumber

#maxlostforever

print(maxInt(numberlist))

#maxfound
