class User:

    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.family} is {self.age}"


me = User('mohammad', 'ordookhani', 24)

you = User('sara', 'moradi', '20')

print(me)
print(you)

me.name
me.family
me.age
print(type(me))
