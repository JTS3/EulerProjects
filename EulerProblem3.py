#Project Euler 3  largest prime factor (http://projecteuler.net/problem=3)
# The original problem specifies 600851475143 but this is more general. 

CandidateNumber = input("What is the candidate number?")
PrimeFactors = []
a = CandidateNumber
n = 2

while n <= CandidateNumber:
    if a % n == 0: 
        PrimeFactors.append(n)
        a = a/n
        print a
    else: n+=1
    
print("", PrimeFactors)
print("The biggest prime factor is:",max(PrimeFactors))