s1 = "abc123xyz45"

# Get all digits from the string
digits = [int(char) for char in s1 if char.isdigit()]

# Calculate sum and average
total = sum(digits)
average = total / len(digits)

print("Sum:", total)
print("Average:", average)
