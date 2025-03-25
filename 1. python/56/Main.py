class Person:
    users = ['mohammad','milad']

    def __init__(self,name):
        self.name = name


me = Person('mohammad')

# print(Person.users)
# Person.users = ['sara']
# print(me.users)


print(Person.users)

print(me.users)

me.users = ['sara']

print(Person.users)