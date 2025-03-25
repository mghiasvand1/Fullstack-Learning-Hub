# list

# myNumbers = [1, 2, 3, 4, 5, 6]

# print(myNumbers[0])
# print(myNumbers[1])
# print(myNumbers[2])
# print(myNumbers[3])
# print(myNumbers[4])
# print(myNumbers[5])

myColors = ["red", "blue", "green", "gray", "yellow", "orange", 3.6]

for color in myColors:
    if type(color) == str:
        print(f"the color is : {color}")
    else:
        print(f"{color} is not a color")

print('--------------------------')

# myColors length = 7
# myColors Last Index = 6

index = 0
while index < len(myColors):
    color = myColors[index]
    if type(color) == str:
            print(f"the color is : {color}")
    else:
        print(f"{color} is not a color")
        
    index += 1
