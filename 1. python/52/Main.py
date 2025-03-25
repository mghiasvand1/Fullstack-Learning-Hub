class User:
    userName = "mohammad"
    userFamily = "ordookhani"
    userAge = 24

    def showFullName(self):
        return f"{self.userName} {self.userFamily}"

    def __init__(self, userName, userFamily):
        self.userName = userName
        self.userFamily = userFamily


mohammad = User("mohammad", "ordookhani")

ali = User("ali", "safari")

print(mohammad.showFullName())
print(ali.showFullName())

print(mohammad.userName + " " + mohammad.userFamily)

