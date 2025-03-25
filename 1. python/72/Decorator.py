def my_decorator(func):
    def say_bye(*args, **kwargs):
        print("this is working for me")
        func(*args, **kwargs)

    return say_bye


@my_decorator
def say_hello(name):
    print(f"hello {name}")


@my_decorator
def say_my_name(name, family):
    print(f"{name} {family}")


# say_hello('mohammad')
say_my_name('mohammad', 'ordookhani')

# sayHelloByDecorator = my_decorator(say_hello)

# sayHelloByDecorator()
