# 2 < age < 8 => 2 dollars
# age >= 65 => 5 dollars
# rest => 10 dollars

age = 50

if (age >= 0 and age <= 2) or (age >= 8 and age < 65):
    print("you should pay 10 dollars")


if not ((age > 2 and age < 8) or age >= 65):
    print("you should pay 10 dollars")
