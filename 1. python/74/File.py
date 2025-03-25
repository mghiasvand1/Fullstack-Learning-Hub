# testTextFile = open("./text.txt")
# print(testTextFile.read())
# testTextFile.seek(1)
# print(testTextFile.read())
# print(testTextFile.readline())
# print(testTextFile.readline())
# print(testTextFile.readline())

# textLines = testTextFile.readlines()
# print(textLines)
#
# testTextFile.close()

# print(testTextFile.read())

# print("hello my name is mohammad")


# with open("./text.txt") as File:
#     print(File.read())
#     File.seek(0)
#     print(File.read())


with open("./text.txt", mode='a') as File:
    File.write('this is edited text\n')

with open("./text.txt", mode='a') as File:
    File.write('this is new test text\n')
