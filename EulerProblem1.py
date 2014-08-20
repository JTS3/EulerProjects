# The following responds to Problem 1 on Project Euler (https://projecteuler.net/problem=1)

TopNumber = input("What is the top number?")
MultipleList = []
n = 1

while n < TopNumber:
    if n % (5 * 3) == 0 : MultipleList.append(n)
    elif n % 5 == 0 : MultipleList.append(n)
    elif n % 3 == 0 : MultipleList.append(n)
    n += 1

print "The multiples of 5 and 3 up to", TopNumber, "are:", MultipleList, "."
print "The sum of these multiples is", sum(MultipleList), "."