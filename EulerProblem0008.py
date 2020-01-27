#Project Euler 8  Largest product in a series (http://projecteuler.net/problem=8)
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

#Get the big number by reading the webpage
from urllib.request import urlopen
page = urlopen("http://projecteuler.net/problem=8")
html = page.read()
thenumber = html.decode("utf-8") #This turns it from a bytes to a string object
#search for the string 73167176 to begin the number, continue until 52963450 to end it and remove breaks
a=thenumber.find("73167176")
b=thenumber.find("52963450")+8
thenumber = thenumber[a:b]
thenumber = thenumber.replace("<br />\n","")


#Solve the problem
ndigits = 4
largestproduct = 0 #this is just the starting value
for i in range(0,1000-ndigits+1):       #go through each substring of the number
    subnumber = thenumber[i:i+ndigits]  #call that a subnumber
    if subnumber.find("0")>0:           #if the subnumber has a zero, then ignore it. The product will be zero.
        currentproduct = 0 
    else:                               #else calculate a product
        currentproduct = 1              #this is just a starting value
        for j in range(0,ndigits):
            currentproduct = currentproduct*int(subnumber[j])
    if largestproduct<currentproduct:
        largestindex = i
        largestproduct = max(largestproduct,currentproduct)

print("The greatest product of ",ndigits,"consecutive digits is found between digits", largestindex, "to",largestindex+ndigits,"and is", largestproduct)