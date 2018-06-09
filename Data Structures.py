numbers = []
n = 0
while n < 6:
    numbers.append(int(input("Please enter a number: ")))
    n += 1
total = 0
for i in reversed(numbers):
    print (i)
    total += i
    i +=1

avg = total/6
print ("Average:",avg)
print ("Total:",total)
