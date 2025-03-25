listNumbers = [1, 2, 3, 4, 5]

tupleNumbers = (1, 2, 3, 4, 5, 2, (4, 5, 3), 3, 3)  # immutable list

# print(3 in tupleNumbers)

newTuple = tuple([1, 2, 3, 4, 5])

# print(newTuple)

locations = {
    (35.67, 45.78): "Tehran",
    (40.30, 69.92): "Shiraz"
}

# print(locations[(35.67, 45.78)])

# for num in tupleNumbers:
#     print(num)


# print(tupleNumbers.count(3))

# print(tupleNumbers.index(3))

# print(tupleNumbers[6][1])

print(tupleNumbers[0:2])