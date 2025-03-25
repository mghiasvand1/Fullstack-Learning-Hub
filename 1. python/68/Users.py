class User:
    ActiveUsers = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        userDict = {'name': name, 'age': age}
        User.ActiveUsers.append(userDict)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(User.ActiveUsers):
            person = User.ActiveUsers[self.index]
            self.index += 1
            return person
        raise StopIteration


person_1 = User('mohammad', 24)
person_2 = User('sara', 20)
person_3 = User('ali', 60)

# print(User.ActiveUsers)

for person in person_1:
    print(person)
