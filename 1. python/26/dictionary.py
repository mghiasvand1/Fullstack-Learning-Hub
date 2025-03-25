# list
# myNumbers = [1, 2, 3, 4, 5, 6]

# names = ["mohammad", "milad", "iman"]

# test = ["Python", True, 5, [4, 5, 6]]

# # dictionary = {
# #     key: value
# # }

# myDictionary = {
#     "name": "Item 1",
#     "Count": 3,
#     "Price": 2500,
#     3: "test"
# }

# myShoppingCart = [
#     {"name": "Python", "price": "free"},
#     {"name": "Kotlin", "price": 2500}
# ]

# myDictionary_2 = dict(name="new Dictionary", age=25)

# print(myDictionary)
# print("------------------")
# print(myDictionary_2)


# print(myDictionary_2["name"])

me = {
    "name": "Mohammad",
    "family": "Ordookhani",
    "age": 24
}

# print(me["name"])
# print(me["family"])
# print(me["age"])

# print(me.values())
# print(me.keys())

# for value in me.values():
#     print(value)

# for key in me.keys():
#     print(me[key])


for key, value in me.items():
    print(key, value)
