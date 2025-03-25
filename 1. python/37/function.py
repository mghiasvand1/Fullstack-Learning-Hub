# def sum_all_numbers(*args):
#     print(args)
#     total = 0
#     for num in args:
#         total += num
#     return total


# numbers = [1, 2, 3, 4, 5, 6]


# print(sum_all_numbers(numbers))  # ([1,2,3,4,5,6],)

# print(sum_all_numbers(*numbers))  # (1,2,3,4,5,6)


# print(sum_all_numbers('second', 4))
# print(sum_all_numbers('third', 1, 5, 6, 9))


# def showUserInfo(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")


# showUserInfo(name="mohammad", family="orodookhani",
#              age=23, email="moh96ordo@gmail.com")



def display_names(name,family):
    print(f"name is {name} and family is {family}")

person = {"name":"sara","family":"moradi"}

display_names(**person)




# parameters
# *args
# default parameters
# **kwargs

# def display_info(a, b, *args, defPara="defalut", **kwargs):
#     return [a, b, args, defPara, kwargs]


# print(display_info(1, 2, 6, first_name="mohammad", last_name="ordookhani"))
