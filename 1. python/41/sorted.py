numbers = [1, 5, 8, 4, 6, 2]

users = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 23},
    {'name': 'taha', 'family': 'ordookhani', 'age': 40},
    {'name': 'ali', 'family': 'ordookhani', 'age': 30},
    {'name': 'sara', 'family': 'ordookhani', 'age': 80}
]


print(sorted(users, key=lambda user: user['age'], reverse=True))

# print(numbers)

# numbers.sort()

# print(numbers)


# result = sorted(numbers, reverse=True)

# print(result)

# print(numbers)
