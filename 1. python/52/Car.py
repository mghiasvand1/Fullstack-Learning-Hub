class Car:

    def __init__(self, name, numberOfDoors, color):
        self.name = name
        self.numberOfDoors = numberOfDoors
        self.color = color

    def showCarFullInfo(self):
        return f"car name is {self.name} & car color is {self.color}"


benz = Car("sls", 2, "red")
benz_2 = Car("test", 2, "yellow")

print(benz.showCarFullInfo())
print(benz_2.showCarFullInfo())
