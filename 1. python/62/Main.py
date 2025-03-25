class Person:
    def __init__(self, name):
        print("Person Init")
        self.__name = name

    def sayHello(self):
        return f"hello {self._Person__name} in Person Class"

    def sayBye(self):
        return f"goodbye {self._Person__name}"


class User:
    def __init__(self, name):
        print("User Init")
        self.__name = name

    def sayHello(self):
        return f"hello {self._User__name} in User Class"


class Admin(Person, User):
    def __init__(self, name):
        print("Admin Init")
        print(f'got name is {name}')
        # super().__init__(name)
        User.__init__(self, 'user name')
        Person.__init__(self, 'person name')


person_1 = Admin('mohammad')

# __mro__
# mro()
# help(cls)

# print(Admin.__mro__)
# print(Admin.mro())
# help(Admin)

# print(person_1._Person__name)
# print(person_1._User__name)


# print(person_1.sayBye())

# print(person_1.name)

# print(person_1.sayHello())

# print(isinstance(person_1, Admin))
# print(isinstance(person_1, User))
# print(isinstance(person_1, Person))
