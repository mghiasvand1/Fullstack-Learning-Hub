myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# doubled_numbers = []
# for num in myNumbers:
#     doubled_numbers.append(num * 2)

doubled_numbers = [num * 2 for num in myNumbers]

print(myNumbers)
print(doubled_numbers)


myName = "Mohammad"
namesCharacters = [char.upper() for char in myName]
print(namesCharacters)

print("-------------------------------")

even = [num for num in myNumbers if num % 2 == 0]

odd = [num for num in myNumbers if num % 2 != 0]

print(even)
print(odd)

newList = [num * 2 if num % 2 == 0 else num * 3 for num in myNumbers]

print(newList)
