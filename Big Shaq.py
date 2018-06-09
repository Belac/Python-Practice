"""
Big Shaq's Song Extravaganza
"""
import random
x=1
while x == 1:
    print ("""
    Yo, Big Shaq, the one and only
    Man's not hot, never hot
    Skrrat, skidi-kat-kat
    Boom
    """)
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    numans = num1 + num2
    numans2 = numans - num3
    print (num1,"plus",num2,"is",numans,", minus",num3,"that's",numans2,", quick maths")
