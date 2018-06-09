list1 = [2,4,2,4,5,10]
list2 = [8,3,6,1,9]

print (list1)
print (list2)
print ("\n\n\n\n")

n = 0
count = 0
try:
    while count < len(list1) and count < len(list2):
        print (list1[n])
        print (list2[n])

        print ("The sum of the numbers is: ", list1[n]+list2[n])
        print ("\n\n")
        n = n + 1
        count = count + 1
except:
    print ("      ¡¡¡ CANNOT ADD !!!")
    print ("¡¡¡ THERE HAS BEEN AN ERROR !!!")
