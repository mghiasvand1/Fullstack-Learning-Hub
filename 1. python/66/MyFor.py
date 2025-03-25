def my_for(iterable, func):
    iterator = iter(iterable)

    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:
            func(thing)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def square(num):
    print(num ** 2)


my_for(numbers, square)
