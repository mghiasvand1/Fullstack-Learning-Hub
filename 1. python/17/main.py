# example



# for num in range(1,10):
#     print("*" * num)


for num in range(1, 10):  # [1,2,3,4,5,6,7,8,9]
    stars = ""
    for star in range(1, num + 1):  # [1, ..., num]
        stars += "*"
    print(stars)
