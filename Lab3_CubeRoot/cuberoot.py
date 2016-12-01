#Brett Piatek
#7/31/16
#COSC1336
#Lab 3- Cube Root

A = 0
X = float(input("Please enter a number:"))        
A = 1/3 *( X/(X*X) + 2 * X)                      

for i in range(0,10):
    difference = X - A * A * A      
    print("For: ", X, "\tGuess", A, "\tDifference: ", difference)
    A = (A + X/A)/3

print("The cube root of", X, "is", A) 