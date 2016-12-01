from math import * 
#num1 = 2 test
#num2 = 5 test
def powerval(num1,num2):
	if num1>num2:
		big = num1
		small = num2	
	#if num1==num2:
		#print("nums are equal! try again!")
	if num1<num2:
		small = num1
		big = num2
	return(int(pow(big,small)))
	#print(big,small) test 