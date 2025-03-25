# decorator


class User:
    activeUsers = 0

    def __init__(self, name, family):
        self.name = name
        self.family = family
        User.activeUsers += 1
        print(f"{self.name} logged in")

    def logOut(self):
        User.activeUsers -= 1
        print(f"{self.name} has logged out")

    @classmethod
    def getActiveUsersCount(cls):
        print(f"there are currently {cls.activeUsers} active users")

    @classmethod
    def from_string(User, string_data):
        name, family = string_data.split(',')
        # return cls(data[0],data[1])
        return User(name,family)



# User.getActiveUsersCount()
# me = User('mohammad', 'ordookhani')
# you = User('sara', 'moradi')
# # me.getActiveUsersCount()
# User.getActiveUsersCount()

print(dict.fromkeys([1, 2, 3], 'hello'))

newInstance = User.from_string("asghar,molodi")

print(newInstance.name, newInstance.family)
