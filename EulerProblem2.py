# The following responds to Problem 2 on Project Euler (https://projecteuler.net/problem=2)
# The problem specifies 4,000,000 as the top number, but this program allows any input number. Be careful with it.

TopNumber = input("This program gives you the sum of the even elements of a sub-sequence -- up to a given top number -- of the Fibonacci sequence.  What is the top number in the Fibonacci sub-sequence?")

FibList = [1, 2]
n = 0
while FibList[n+1] < TopNumber:
    NextNumber = FibList[n+1] + FibList[n] 
    if ( NextNumber > TopNumber) : break
    FibList.append(NextNumber)
    n += 1    
print "The Fibbonacci sub-sequence terminating in the highest number less than", TopNumber,"is", FibList, "."


TempEvenFibSum = 0
x = 1
while x < len(FibList):
    EvenFibSum = TempEvenFibSum + FibList[x] 
    x += 2
    TempEvenFibSum = EvenFibSum
print "The sum of the even numbered elements of the subsequence is ", EvenFibSum, "."