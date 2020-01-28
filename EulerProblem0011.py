#Project Euler 11  Largest product in a grid (http://projecteuler.net/problem=11)
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

#Get the big number by reading the webpage
from urllib.request import urlopen
page = urlopen("http://projecteuler.net/problem=11")
html = page.read()
thenumber = html.decode("utf-8") #This turns it from a bytes to a string object
#search for the strings to begin the grid and end it and remove breaks
a=thenumber.find("08 02 22 97 38 15 00 40")
b=thenumber.find("61 43 52 01 89 19 67 48")+23
thenumber = thenumber[a:b]
thenumber = thenumber.replace("<span style=\"color:#ff0000;\"><b>","")
thenumber = thenumber.replace("</b></span>","")
thenumber = thenumber.replace("<br />\n","; ")
#need to get rid of leading zeros, this is not the greatest fix
thenumbers = thenumber.split()
thenumbers = [i.replace("00","0") for i in thenumbers]
thenumbers = [i.replace("01","1") for i in thenumbers]
thenumbers = [i.replace("02","2") for i in thenumbers]
thenumbers = [i.replace("03","3") for i in thenumbers]
thenumbers = [i.replace("04","4") for i in thenumbers]
thenumbers = [i.replace("05","5") for i in thenumbers]
thenumbers = [i.replace("06","6") for i in thenumbers]
thenumbers = [i.replace("07","7") for i in thenumbers]
thenumbers = [i.replace("08","8") for i in thenumbers]
thenumbers = [i.replace("09","9") for i in thenumbers]
thenumbers = " ".join(thenumbers)

import numpy as np
thegrid = np.matrix(thenumbers) 

ndigits = 4
largestproduct=0
#Solve the problem
for i in range(0,20): #row
    for j in range(0,20): #column
        for k in ["NS","WE","NWSE","SWNE"]: #direction
            tempmat = np.matrix([0]) #initialize the temporary matrix as a 1 element matrix
            if k == "NS": #Get the elements up and down 
                tempmat = thegrid[i:i+ndigits,j]
            if k == "WE": #Get the elements left to right
                tempmat = thegrid[i,j:j+ndigits]
            if k == "NWSE": #Get The elements NW to SE
                tempmat = thegrid[i:i+ndigits,j:j+ndigits].diagonal(0,1,0)
            if k == "SWNE":  #Get the elements SW to NE
                tempmat = np.fliplr(thegrid[i:i+ndigits,j:j+ndigits]).diagonal(0,1,0)
            if tempmat.size == ndigits:
                candidateproduct = tempmat.prod()
                if candidateproduct>largestproduct:
                    largesti = i #Note the coordinates i,j,k
                    largestj = j
                    largestk = k
                    largestproduct = candidateproduct
                #print(i,j,k,tempmat.prod())

print("The greatest product of ",ndigits,"consecutive elements in the matrix is found at row", largesti,"and column", largestj,"(remember 0-indexing in Python) in the",largestk,"direction and is", largestproduct)
