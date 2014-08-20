# The following responds to Problem 1 on Project Euler (https://projecteuler.net/problem=1)

TopNumber = input("What is the top number?")
MultipleList = []
CandidateMultiple = 1

while CandidateMultiple < TopNumber:
    if CandidateMultiple % (5 * 3) == 0 : MultipleList.append(CandidateMultiple)
    elif CandidateMultiple % 5 == 0 : MultipleList.append(CandidateMultiple)
    elif CandidateMultiple % 3 == 0 : MultipleList.append(CandidateMultiple)
    CandidateMultiple += 1

print "The multiples of 5 and 3 up to", TopNumber, "are:", MultipleList, "."
print "The sum of these multiples is", sum(MultipleList), "."