# parameters


# def sum(firstNumber):
#     return firstNumber + 6


# print(sum(5))
# print(sum(9))

# def sum(firstNumber, secondNumber):
#     return firstNumber + secondNumber

# print(sum(19,6))

# name = "mohammad"
# family = "ordookhani"

# person = {
#     "name": "mohammad",
#     "family": "ordookhani"
# }


# def showFullName(firstName, lastName):
#     return f"{firstName} {lastName}"


# print(showFullName(name, family))
# print(showFullName(person["name"], person["family"]))


# def divide(num_1, num_2):
#     return num_1 / num_2

# print(divide(3,5))
# print(divide(5,3))


# myNumbers = [1, 2, 3, 4, 5, 6, 7]  # 16

# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total


# print(sum_odd_numbers(myNumbers))


def is_even_number(number):
    if number % 2 == 0:
        return True
    return False


print(is_even_number(5))  # false
print(is_even_number(6))  # true
