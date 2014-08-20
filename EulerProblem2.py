# The following responds to Problem 2 on Project Euler (https://projecteuler.net/problem=2)
# The problem specifies 4,000,000 as the top number, but this program allows any input number. Be careful with it.

TopNumber = input("This program gives you the sum of the even elements of a sub-sequence -- up to a given top number -- of the Fibonacci sequence.  What is the top number in the Fibonacci sub-sequence?")

FibList = [1, 2]
IndexA = 0
while FibList[IndexA+1] < TopNumber:
    NextNumber = FibList[IndexA+1] + FibList[IndexA] 
    if ( NextNumber > TopNumber) : break
    FibList.append(NextNumber)
    IndexA += 1    
print "The Fibbonacci sub-sequence terminating in the highest number less than", TopNumber,"is", FibList, "."


TempEvenFibSum = 0
IndexB = 1
while IndexB < len(FibList):
    EvenFibSum = TempEvenFibSum + FibList[IndexB] 
    IndexB += 2
    TempEvenFibSum = EvenFibSum
print "The sum of the even numbered elements of the subsequence is ", EvenFibSum, "."