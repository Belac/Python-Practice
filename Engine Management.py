"""
Tesla Engine Management System
"""

import random
import time

print ("                 Tesla's Engine Management\n")
time.sleep(1)
print ("        ----------------------------------------------")
time.sleep(1)
print ("This software will provide temperatures every second.")
print ("In this simulation, time has been sped up to increase temperature variability.\n\n\n\n")
time.sleep(4)
count = 0


internalTemp = random.randint(-5,25)
externalTemp = random.randint(-10,25)

while True:
    count = random.randint(0,10)
    if count <= 5:
        internalTemp = internalTemp + 1
        externalTemp = externalTemp + 1
    else:
        internalTemp = internalTemp - 1
        externalTemp = externalTemp - 1
    if internalTemp > 30 or externalTemp > 30:
        internalTemp = internalTemp - 2
        externalTemp = externalTemp - 2
    print ("Internal Temperature:",internalTemp,"°C")
    print ("External Temperature:",externalTemp,"°C")
    if internalTemp <= 16:
        print ("Air Conditioning is Inactive.")
        print ("Heating is Active.")
        print ("Engine is off.\n")
    else:
        print ("Air Conditioning is Active.")
        print ("Heating is Inactive.")
        print ("Engine is off.\n")
    time.sleep(1)
    
