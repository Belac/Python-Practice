"""
The Fibonacci Sequence
"""

def mystery(n): #This defines a procedure, and gives it a name
    a, b = 0, 1 #This assigns the two numbers to two seperate variables
    while a < n: #This creates a while loop which runs whilst a is less than n
        print (a) #This prints the variable 'a' to the screen
        a, b = b, a + b #This assigns b to a, and a + b to b

mystery(10) #This runs the set function
