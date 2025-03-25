# filter()

numbers = [1, 2, 3, 4, 5, 6]

evens = filter(lambda num: num % 2 == 0, numbers)

# print(list(evens))


users = [
    {'name': 'mohammad', 'shopCart': []},
    {'name': 'sara', 'shopCart': ['kotlin', 'vue']},
    {'name': 'iman', 'shopCart': []}
]

# print(len(users))

# result = filter(lambda user: len(user['shopCart']) == 0, users)
result = filter(lambda user: not user['shopCart'], users)

# print(list(result))


result2 = map(lambda user: user['name'],
              filter(lambda user: not user['shopCart'], users)
              )

print(list(result2))

result3 = [user['name'] for user in users if len(user['shopCart']) == 0]

print(result3)