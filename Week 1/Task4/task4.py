# Task 4 - calculate the factorial

n = int(input("Input a number to calculate the factorial of: "))

fakultaet = 1
for i in range(1, n + 1):
    fakultaet *= i

print("The factorial of " + str(n) + " is: " + str(fakultaet))
