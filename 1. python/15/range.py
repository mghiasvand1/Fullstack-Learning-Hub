# range() => to create a list of numbers
# 1 , 2 , 3 , ... , 10

# print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
# print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# for num in range(1, 10):
#     print("*" * num)


for num in range(1, 10):
    if num % 2 == 1:
        for star in range(1, 6):  # [1, 2, 3, 4, 5]
            print("*" * star)
    else:
        for star in range(5, 0, -1):  # [5, 4, 3, 2, 1]
            print("*" * star)
