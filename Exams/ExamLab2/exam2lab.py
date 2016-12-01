#http://www.co-pylit.org/html/C78P43/ExamTwoLab.html
#Brett Piatek
#7/20/2016
#CS1336
#Exam 2 Lab
from mymath import *

examnum = "Exam 2 Lab"
first = "Brett"
last = "Piatek"
month = "July"
day = "21"
year = "2016"
print("%s"%(examnum))
print("Submitted by:%s %s"%(first,last))
print("%s %s,%s"%(month,day,year))
def getData():
	stuff = []
	fin = open("sample.dat","r") #Opens the data file
	for i in range(15): #loops the readline to read the entire list
		nums = int(fin.readline().strip())
		stuff.append(nums)
	return stuff
def summer(data):
	sum = 0
	n = 0
	for i in range (7):
		sum += powerval(data[n], data[n+1])
		n += 2
	return sum
		
print("The final sum was", summer(getData()))
