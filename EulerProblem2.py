# The following responds to Problem 2 on Project Euler (https://projecteuler.net/problem=2)
# The problem specifies 4,000,000 as the top number, but this program allows any input number. Be careful with it.

TopNumber = int(input("What is the top number in the Fibonacci sub-sequence?"))

i = 1
j = 2
FibList = [i, j]
n = 0

while FibList[n+1] < TopNumber:
    NextNumber = FibList[n+1] + FibList[n] 
    if ( NextNumber > TopNumber) : break
    FibList.append(NextNumber)
    n += 1
    
print("The Fibbonacci sub-sequence terminating in the highest number less than", TopNumber,"is", FibList, ".")

x = 1
a = 0
while x < len(FibList):
    EvenSumTemp = a + FibList[x] 
    x += 2
    a = EvenSumTemp
print("The sum of the even numbered elements of the subsequence is ", EvenSumTemp, ".")