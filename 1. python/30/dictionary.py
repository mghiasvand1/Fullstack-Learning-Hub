# numbers = [1, 2, 3, 4, 5]

# doubledNumbers = [num * 2 for num in numbers]

# print(doubledNumbers)

numbers = dict(first=1, second=2, third=3)

squaredNumbers = {key: value ** 2 for key, value in numbers.items()}

print(squaredNumbers)

# simpleNumbers = {num: num for num in [1, 2, 3, 4, 5]}

simpleNumbers = {num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4, 5]}

print(simpleNumbers)

