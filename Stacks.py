#----------------Creating a Class----------------#
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def contents(self):
        return self.items

#----------------------Main----------------------#
userInput = ("Enter a word or phrase to be tested: ")
stackOne = Stack()
stackTwo = Stack()
stackThree = Stack()

for i in userInput:
    stackOne.push(i)

for x in stackOne.contents:
    stackTwo.push(x)

for n in stackTwo.contents():
    stackThree.push(stackTwo.pop())

if stackOne.contents == stackTwo.contents:
    print ("It is a palendrome.")
else:
    print ("It is not a palendrome.")