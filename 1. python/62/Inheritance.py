# method resolution order

# __mro__
# mro()
# help(cls)


class A:
    def say_hello(self):
        print("hello python in A")


class B(A):
    pass
    # def say_hello(self):
    #     print("hello python in B")


class C(A):
    pass
    # def say_hello(self):
    #     print("hello python in C")


class D(C, B):
    pass
    # def say_hello(self):
    #     print("hello python in D")


item = D()

# item.say_hello()

print(help(D))