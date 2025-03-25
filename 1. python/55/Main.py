class User:
    def __init__(self, gotName, gotFamily, gotAge):
        self.name = gotName
        self.family = gotFamily
        self.age = gotAge

    def showFullName(self):
        return self.name + ' ' + self.family
        # return f"{self.name} {self.family}"

    def userAgeStatus(self):
        return "adult" if self.age > 18 else "not adult"


me = User('mohammad', 'ordookhani', 12)
you = User('sara', 'moradi', 20)

print(me.showFullName())
print(me.userAgeStatus())