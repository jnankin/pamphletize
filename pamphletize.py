import math, sys, os
from fabric.operations import local

inputFilename = "input.pdf"
outputFilename = "output.pdf"

with open(inputFilename): pass
    
n = int(local('pdfinfo {0} | grep Pages: | awk \'{{print $2}}\''.format(inputFilename), capture=True).splitlines()[-1])

if (n % 4 != 0):
	print "Number of pages in input must be divisible by 4"
	raise 

print "Num pages: {0}".format(n)

totalPaperPages = int(math.ceil(n / 4.0))

pdfTkCommand = "pdftk {0} shuffle ".format(inputFilename)

for i in range(0, totalPaperPages):	
		front = str((n - (2*i))) + ' ' + str(((2 * i) + 1)) 
		back = str(((2 * i) + 2)) + ' ' + str((n - (2*i) - 1))
		pdfTkCommand = pdfTkCommand + " " + front + " " + back + " "

pdfTkCommand = pdfTkCommand + " output " + outputFilename

local(pdfTkCommand)
