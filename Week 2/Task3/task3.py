# Original list of dictionaries
cars = [
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sort the list using lambda
sorted_cars = sorted(cars, key=lambda x: x['make'].strip())

# Print the sorted list
print(sorted_cars)
