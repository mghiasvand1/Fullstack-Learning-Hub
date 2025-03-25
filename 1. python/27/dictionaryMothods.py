me = {
    "name": "mohammad",
    "family": "ordookhani",
    "age": 24,
    "email": "moh96ordo@gmail.com"
}

# print(me)
# me.clear()
# print(me)

# copy_me = me.copy()
# print(me)
# print(copy_me)

# print(me == copy_me)
# print(me is copy_me)


# generate default value

# newUser = {"name": "unknown", "family": "unknown"}

# newUser_2 = dict.fromkeys(["name","family"], "unknown")

# print(newUser_2)


# get

# print(me["phone"])

print(me.get("phone"))

isPhoneExist = me.get("phone")

print(isPhoneExist is None)

# if "phone" in me:
#     print("is exist")
