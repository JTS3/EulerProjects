# The following responds to Problem 2 on Project Euler (https://projecteuler.net/problem=2)
# The problem specifies 4,000,000 as the top number, but this program allows any input number. Be careful with it.
print "  "
print "This program gives you the sum of the even elements of a sub-sequence -- up to a given top number -- of the Fibonacci sequence."
top_number = input("What is the top number in the Fibonacci sub-sequence?")

fib_list = [1, 2]
indexA = 0
while fib_list[indexA+1] < top_number:
    next_number = fib_list[indexA+1] + fib_list[indexA] 
    if ( next_number > top_number) : break
    fib_list.append(next_number)
    indexA += 1    
print "The Fibonacci sub-sequence terminating in the highest number less than", top_number,"is", fib_list, "."


even_fib_sum = 0
indexB = 1
while indexB < len(fib_list):
    even_fib_sum += fib_list[indexB] 
    indexB += 2
print "The sum of the even numbered elements of the subsequence is ", even_fib_sum, "."