print("\nWelcome to Ardunio!\n\nHow many units would you like?\n\n1-9: $29.95/unit\n10-49: $26.96/unit")
unitNum = int(input("Please enter a number: "))
lowOrder = 29.95 
highOrder = 26.96 
lowTotal = unitNum * lowOrder
highTotal = unitNum * highOrder
finalTotal = "Your order total is: "
if (unitNum <= 9): 
	print("\nGot it! Your total price of Units is: ")	
	print(unitNum * lowOrder)
else:
	print("\nGot it! Your total price of Units is: ")
	print(unitNum * highOrder)
if (unitNum <= 20):
	print("\n7 days (USPS Priority): $4.72\n5 days (UPS Groud): $9.60\n3 days (UPS Express): $12.84\n1 day (UPS Overnight): $29.94\n")
else: 
	print("\n7 days (USPS Priority): $10.94\n5 days (UPS Groud): $17.50\n3 days (UPS Express): $16.46\n1 day (UPS Overnight): $36.81\n")
mailTime = int(input("Which shipping option would you like? (Enter by number of days): "))
if (unitNum <= 20):
	if (mailTime == 7):
		print(finalTotal)
		print(lowTotal + 4.72)
	if (mailTime == 5):
		print(finalTotal)
		print(lowTotal + 9.60)
	if (mailTime == 3):
		print(finalTotal)
		print(lowTotal + 12.84)
	if (mailTime == 1): 
		print(finalTotal)
		print(lowTotal + 29.94)
if (unitNum > 20):
	if(mailTime == 7):
		print(finalTotal)
		print(highTotal + 10.94)
	if(mailTime == 5):
		print(finalTotal)
		print(highTotal + 17.50)
	if(mailTime == 3):
		print(finalTotal)
		print(highTotal +16.46)
	if(mailTime == 1):
		print(finalTotal)
		print(highTotal + 36.81)