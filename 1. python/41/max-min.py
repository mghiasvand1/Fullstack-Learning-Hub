numbers = [3, 6, 8, 13, 4, 90]

chars = ['a', 't', 'z']

myName = "mostafa"

names = ['mohammad', 'milad', 'akbar', 'sara', 'iman','ali']

res = [len(name) for name in names]

print(res)

# print(max(numbers))

# print(min(numbers))

print(max(names, key=lambda n: len(n)))
print(min(names, key=lambda n: len(n)))
