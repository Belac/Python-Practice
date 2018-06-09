"""
Recursion
"""
"""
Recursion is when a procedure/function calls its from within itself
e.g
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)

"""
import mathlib

no = int(input("Enter a number: "))
print (mathlib.Factorial(no))

def Factorial2(no):
    while no > 1:
        return no * Factorial2(no-1)
    if no == 0:
        return 1

print (Factorial2(no))
