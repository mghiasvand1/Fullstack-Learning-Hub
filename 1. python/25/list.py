# nested lists

numbers = [1, 2, 3, 4, 5, 6]

newNumbers = [[1, 2, 3], [4, 5, 6]]

# index_1 = newNumbers[1]  # [4, 5, 6]

# number_6 = index_1[2]  # 6

# number = newNumbers[1][2]  # 6

# print(number)

# print('------------------------------')

# for li in newNumbers:
#     for num in li:
#         print(num)

# print('------------------------------')

# copyList = [[print(l) for l in li] for li in newNumbers]

# print(copyList)


generatedList = [num for num in range(1, 4)]

generatedNestedList = [
    ['X' if newNum % 2 == 0 else 'O' for newNum in range(1, 4)] for num in range(1, 4)]

print(generatedList)
print(generatedNestedList)
