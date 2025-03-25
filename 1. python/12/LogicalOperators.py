# logical operators

# and , or , not


# and

userAge = 17
userGender = "female"

if userAge >= 18 and userGender == "male":
    print("you have to go to soldiery")
else:
    print("you can stay at home")

print("-------------------")
print(f"True and True : { True and True }")
print(f"False and True : { False and True }")
print(f"True and False : { True and False }")
print(f"False and False : { False and False }")


# or

print("------------------")

weather = "sunny"

if weather == "sunny" or weather == "cloudy":
    print("we can travel")
else:
    print("we can not travel")

print("-------------------")
print(f"True or True : { True or True }")
print(f"False or True : { False or True }")
print(f"True or False : { True or False }")
print(f"False or False : { False or False }")


# not

print("------------------------")
isBrotherComming = False

if not isBrotherComming:
    print("my sister said : i wont come")

print("-------------------")
print(f"not True : { not True }")
print(f"not False : { not False }")
