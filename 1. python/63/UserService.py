class IUserService:
    def getAllUsers(self): raise NotImplementedError

    def getUserById(self): raise NotImplementedError

    def createNewUser(self): raise NotImplementedError


class UserServiceBySql(IUserService):
    def getAllUsers(self):
        print("get all users from sql server")

    def getUserById(self):
        print("get user by id from sql server")

    def createNewUser(self):
        print("create new user from sql server")


class UserServiceByOracle(IUserService):
    def getAllUsers(self):
        print("get all users from oracle")

    def getUserById(self):
        print("get user by id from oracle")

    def createNewUser(self):
        print("create new user from oracle")


userService = UserServiceBySql()
userService_by_oracle = UserServiceByOracle()

userService.getAllUsers()
userService.createNewUser()

userService_by_oracle.getAllUsers()
