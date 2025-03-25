me = {
    "name": "mohammad",
    "family": "ordookhani",
    "email": "moh96ordo@gmail.com"
}

# print(me)

# me.pop("name")
# me.popitem()
# me.popitem()


second = {
    "age": 50,
    "name": "milad"
}

print(second)

second.update(me)

print(second)

print("------------------------")

second["namek"] = "sara"

print(second)
