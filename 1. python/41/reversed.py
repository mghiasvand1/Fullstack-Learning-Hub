numbers = [1, 2, 3, 4, 5, 6]

# numbers.reverse()

print(numbers)

print(list(reversed(numbers)))

print(list(reversed("hello")))

# print("hello"[::-1])

nameRes = ''

print(nameRes.join(list(reversed("hello"))))


for num in reversed(range(0, 10)):
    print(num)
