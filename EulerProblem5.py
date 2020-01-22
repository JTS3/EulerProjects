#Project Euler 5  Smallest multiple (http://projecteuler.net/problem=5)
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def SequentialMultipleCheck(target, greatest_integer):
    smallest_integer = 2 #skip 1, anything mod 1 is = 0
    n = smallest_integer
    while n <= greatest_integer:
        if target % n != 0:
            return(False) 
        else:
            n += 1
    return(True)



SequentialMultipleCheck(2520,10)



#now run through the even numbers (it must be even as target % 2 == 0) after 2520 (which we know is the smallest product for the 1 to 10 range)

target = 2520
ENDER = 0
while ENDER == 0:
    if SequentialMultipleCheck(target,20):
        print("HERE",target)
        ENDER = 1
    else:
        print("nope",target)
        target += 2
        #ENDER = 0

#This will do it, but there is a much smarter way to do this... probably taking advantage of primes
