"""
Demonstrating Value Vs. Reference
"""
import mathlib

#Passing parameters by reference
width = int(input("What is the width: "))
height = int(input("What is the height: "))
area = mathlib.RecArea(width,height)
print (area)


#Passing parameters by value
area = mathlib.RecArea(20,10)
print (area)
