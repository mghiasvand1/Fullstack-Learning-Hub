# poly => multi
# morph => form

class Animal:

    def makeSound(self):
        raise NotImplementedError


class Dog(Animal):
    def makeSound(self):
        return "cat is making sound"


class Cat(Animal):
    def makeSound(self):
        return "cat is making sound"


class Worm(Animal):
    def makeSound(self):
        return "worm does not make any sound"


dog = Dog()
cat = Cat()
worm = Worm()

print(cat.makeSound())

print(dog.makeSound())

print(worm.makeSound())

# numbers = [1, 2, 3, 4, 5, 6]
#
# myNums = {1, 2, 3, 4, 5, 6}
#
# person = {
#     'name': 'sara',
#     'family': 'miladi'
# }
#
# numbers.copy()
# myNums.copy()
# person.copy()
#
# print(len(numbers))
# print(len(myNums))
