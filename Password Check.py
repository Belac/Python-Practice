"""
Password Check
"""
n=0
while n == 0:
    passw = input("Input your new password: ")
    if len(passw) < 8 and len(passw) > 10:
        print ("I'll allow it.")
        n = 1
    else:
        print ("""---INVALID---
    Must contain 8-10 characters, at least one capital letter, and one number.""")

