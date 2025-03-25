# list slicing => to make a copy of a list

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

selectedNumber = myNumbers[1]

# some_list[start:end:step]

# selectedNumbersFromList = myNumbers[-5:]

# print(selectedNumbersFromList)

# copyOfNumbers = myNumbers[::2]

# print(myNumbers)
# print(copyOfNumbers)

# print(myNumbers == copyOfNumbers)
# print(myNumbers is copyOfNumbers)

colors = ["red", "green", "blue", "yellow", "orange"]


copyOfColors = colors[::-1]  # ["orange","yellow","blue","green","red"]

colors.reverse()


print(colors)
print(copyOfColors)


print("-----------------------------")

myName = "mohammad ordookhani"

print(myName[:8])
