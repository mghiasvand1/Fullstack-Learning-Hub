class User:
    activeUsersCount = 0
    allowedUsers = ['mohammad', 'milad', 'sara', 'iman']
    loggedInUsers = []

    def __init__(self, userName, userFamily):
        if userName not in User.allowedUsers:
            raise ValueError(f"{userName} can not login !!")

        self.name = userName
        self.family = userFamily
        User.activeUsersCount += 1
        User.loggedInUsers.append(userName)
        # print(f"{self.name} logged in")

    def logOut(self):
        # print(f"{self.name} has logged out")
        User.activeUsersCount -= 1
        User.loggedInUsers.remove(self.name)


mohammad = User('mohammad', 'ordookhani')

sara = User('sara', 'moradi')

print(User.allowedUsers)
User.allowedUsers = ['sara', 'mostafa']

print(mohammad.allowedUsers)
# mohammad.allowedUsers = ['mohammad', 'asghar']
# print(mohammad.allowedUsers)
# print(User.allowedUsers)

# print(User.loggedInUsers)
# print(User.activeUsersCount)
# print(mohammad.activeUsersCount)
#
#
# print(mohammad.allowedUsers == User.allowedUsers)
# print(mohammad.allowedUsers is User.allowedUsers)

# print(id(mohammad.allowedUsers))
# print(id(sara.allowedUsers))
# print(id(User.allowedUsers))

# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
#
# mohammad = User('mohammad', 'ordookhani')
#
# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
#
# sara = User('sara', 'moradi')
#
# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
# sara.logOut()
# mohammad.logOut()
#
# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
