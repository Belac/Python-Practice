"""
Mega Cinema
"""

import time
import sys
from pprint import pprint

cuser = "admin"
cpassw = "pass"
x = 0

movies = {
    "it":{
        "kirkstall": {"8:00","10:00","12:00","16:00","18:00","20:00"},
        "headingley": {"8:00","10:00","12:00","16:00","18:00","20:00"},
        "leedscentre": {"8:00","10:00","12:00","16:00","18:00","20:00"}
        },
    "dunkirk": {
        "kirkstall": {"8:00","10:00","12:00","16:00","18:00","20:00"},
        "headingley": {"8:00","10:00","12:00","16:00","18:00","20:00"},
        "leedscentre": {"8:00","10:00","12:00","16:00","18:00","20:00"}
        }
    }

while x < 4:
    user = input("Username: ")
    passw = input("Password: ")
    if user == cuser:
        if passw == cpassw:
            print("\n")
            time.sleep(0.5)
            print("Loading.\n")
            time.sleep(0.5)
            print ("Loading..\n")
            time.sleep(0.5)
            print ("Loading...\n")
            time.sleep(0.5)
            print ("---------- LOGIN SUCCESSFUL ----------\n\n\n\n")
            x = 4
    elif x == 3:
        sys.exit()
    else:
        print ("INVALID")
        x = x + 1
time.sleep(1)
print ("     Welcome to...\n")
print ("      ~~~~~THE MEGA CINEMA MOVIE DATABASE~~~~~\n\n\n\n")
films = input("Please enter the name of a movie: ")
films = films.lower()

if films in movies:
    print ("\n")
    print ("Venues          Times")
    pprint(movies.get(films))

cinema = input("Please enter a cinema: ")
