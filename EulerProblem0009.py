#Project Euler 9  a pythagorean triple (http://projecteuler.net/problem=9)


#We have the following constraints:
#a^2+b^2=c^2
#a+b+c=1000
#0<a<b<c
#and a,b,c are all integers

#reduce the problem to two variables
#c=1000-(a+b)
#c^2=1000^2-2000(a+b)+(a+b)^2
#c^2=1000^2-2000(a+b)+a^2+2ab+b^2
#a^2+b^2=1000^2-2000(a+b)+a^2+2ab+b^2
#0=1000^2-2000(a+b)+2ab
#0=1000-2(a+b)+ab/500
#0=500-1(a+b)+ab/1000
#a+b-ab/1000=500

output = []
for b in range(1,500+1):
    for a in range(1,b):
        if (a+b)-a*b/1000 == 500:
            output = [a,b,int((a**2+b**2)**.5)]

#check the output
if (sum(output)==1000) and (output[0]**2 + output[1]**2 == output[2]**2):
    print("The Pythagorean triple is", output)
