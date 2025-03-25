class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    @property
    def fullName(self):
        return f"{self.name} {self.family}"


class User(Person):
    def __init__(self, name, family, email):
        super().__init__(name, family)
        # Person.__init__(self, name, family)
        self.email = email


# mohammad = User('mohammad', 'moradi')
#
# print(mohammad.fullName)

sara = User('sara', 'moradi', 'test@test.com')

print(sara.fullName)
