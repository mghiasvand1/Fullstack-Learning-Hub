# map

# numbers = [1, 2, 3, 4, 5]

# doubles = map(lambda x: x * 2, numbers)

# print(doubles)

# print(list(doubles))

# print(list(doubles))

# doubles = [2, 4, 6, 8, 10]

# doubles = []

# for num in numbers:
#     doubles.append(num * 2)

# print(doubles)

names = ["mohammad", "sara", "iman", "ali"]

upperNames = map(lambda name: name.upper(), names)

# print(list(upperNames))


people = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 23},
    {'name': 'sara', 'family': 'moradi', 'age': 25},
    {'name': 'iman', 'family': 'madaeny', 'age': 30}
]

# families = map(lambda person: person['family'], people)

print(list(map(lambda person: person['family'], people)))

# families_2 = []

# for person in people:
#     families_2.append(person['family'])

# print(families_2)