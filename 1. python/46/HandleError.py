# try:
#     print(myName)
# except:
#     print('an error occured')


# def get(d, key):
#     try:
#         return d[key]
#     except KeyError:
#         return "no key found"
#     except IndexError:
#         return "index error"


# person = {
#     'name': 'mohammad',
#     'family': 'ordookhani'
# }

# print(get(person, 'age'))

# while True:
#     try:
#         num = int(input("plese enter a number: "))
#     except ValueError:
#         print('thats not a number! please enter another one :')
#     else:
#         print('you have entered a number')
#         break
#     finally:
#         print('this is finally section')

def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return "Dont Divide By Zero Please !!!"
    except TypeError as error:
        print(error)
        return "first and second must be numbers !!!"


print(divide(1, 'skjdf'))
