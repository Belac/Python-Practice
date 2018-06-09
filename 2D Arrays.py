outletSales = [[10,12,15,10],[5,8,3,6],[10,12,15,10]]
quarterOne = 0
quarterTwo = 0
quarterThree = 0
quarterFour = 0

for outlet in range(0,len(outletSales)):
    quarterOne += outletSales[outlet][0]
    quarterTwo += outletSales[outlet][1]
    quarterThree += outletSales[outlet][2]
    quarterFour += outletSales[outlet][3]

#print(outletSales[outlet][quarter])
print(quarterOne,quarterTwo,quarterThree,quarterFour)
