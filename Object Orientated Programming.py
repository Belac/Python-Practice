class Dog():
    def __init__(self, myName, myColour):
        self.p_name = myName
        self.p_colour = myColour

    def bark(self, barkTimes):
        for n in range (barkTimes):
            print("Woof")

    def setColour(self, myColour):
        self.p_colour = myColour

    def getColour(self):
        return self.p_colour

    def getName(self):
        return self.p_name

    def printDogDetails(self):
        print (self.p_name, self.p_colour)

class Puppy(Dog):
    def __init__(self,myName,myColour):
        self.p_name = myName
        self.p_colour = myColour
        self.shoesChewed = 0

    def chewShoe(self,numShoes):
        self.shoesChewed = self.shoesChewed + numShoes

    def getShoesChewed(self):
        return self.shoesChewed
        
myFirstDog = Dog("Fido", "Black")
mySecondDog = Dog("Bonnie", "Blonde")
myThirdDog = Dog("Mutt", "Unknown")

print(myFirstDog.getName(), "says")
myFirstDog.bark(2)
print("\n")

if myThirdDog.getColour() == "Unknown":
    print ("Please enter colour for", myThirdDog.getName())
    newcolour = input()
    myThirdDog.setColour(newcolour)
print (myThirdDog.getName(), "is now set to", myThirdDog.getColour())

print("\n")
myFirstPuppy = Puppy("Mongrel", "Dirty")
myFirstPuppy.chewShoe(5)
print (myFirstPuppy.getName(),"has chewed",myFirstPuppy.getShoesChewed(),"shoes")
