#FirstWorldProblems

sweets = int(input("How many sweets? "))
bags = int(input("How many bags? "))

def EvenOrOdd(x):
    if x % 2 == 0:
        xooe = "Even"
    else:
        xooe = "Odd"
    return xooe

print ("Bags:",EvenOrOdd(bags))
print ("Sweets:",EvenOrOdd(sweets))
print ("\n\n")

def FirstWorldProblemPossible(x,y):
    if (x == "Even" and y == "Odd") or (x == "Odd" and y == "Even"):
        print ("It's Impossible.")
    else:
        print ("It's Possible.")
