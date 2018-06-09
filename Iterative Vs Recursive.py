"""
Iteration Vs Recursion
"""
import time

fibn = [0,1]

def fib(n):
	if n <= 1:
            return n
	else:
	    return fib(n-1) + fib(n-2)

def fib2(n):
    fibNumbers = [0,1]
    for i = 2 to n:
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
	next i
	return fibNumbers[n] 

iterativeStart = time.clock()
fib2(fibn)
iterativeEnd = time.clock

recursiveStart = time.clock()
fib(fibn)
recursiveEnd = time.clock

iterationTime = (iterativeEnd - iterativeStart)
recursiveTime = (recursiveEnd - recursiveStart)

print (iterationTime)
print (recursiveTime)
