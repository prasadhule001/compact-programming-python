# Given list of tuples
my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort by the last element of each tuple
sorted_list = sorted(my_list, key=lambda x: x[-1])

# Print the result
print(sorted_list)
