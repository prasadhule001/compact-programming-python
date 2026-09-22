# Task 4 - calculate the factorial

n = int(input("Input a number to calculate the factorial of: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("The factorial of " + str(n) + " is: " + str(factorial))
