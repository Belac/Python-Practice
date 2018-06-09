# Binary Search Animals

#Creates a list of animals
nameList = ["baboon","cheetah","elephant","giraffe","hippo","leopard","lion","mongoose","rhino","warthog"]

#Creates the variable 'animal' as 'lion'
animal = "lion"

#Sets the variable found to False (Boolean)
found = False
#The variable 'high' is set to the length of the list of animals, minus one.
high = len(nameList)-1
#Low is set to zero
low = 0
#While found is equal to False, and high is greater than or equal to low.
while found == False and high >= low:
    #Guess is equal to low plus high divided by two into a whole number.
    guess = (low + high) // 2
    #Prints all of the variables
    print (low, " ", high, " ", guess, " ", nameList[guess])
    #If the guess posiiton matches lion, found is set to True
    if nameList[guess] == animal:
        found = True
    #Or, if guess is greater than animal, high is set to guess minus one
    elif nameList[guess] > animal:
        high = guess - 1
    #Otherwise, low is equal to guess plus one
    else:
        low = guess + 1
#If it has found lion, print 'animal found'
if found == True:
    print ("animal found at index ", guess)
#Otherwise, print 'animal not in the list'
else:
    print ("animal not in list")

#Stops the program when the user enters anything.
input("\nPress ENTER to exit program ")
