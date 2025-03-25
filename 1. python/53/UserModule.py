class User:

    def __init__(self, gotUserName="undefined", gotUserFamily='undefined', gotUserAge=0, gotUserEmail='', gotUserPass=''):
        self.userName = gotUserName
        self.userFamily = gotUserFamily
        self.userAge = gotUserAge
        self.userEmail = gotUserEmail
        self.userPass = gotUserPass

    def buyCourse(self):
        return f"{self.userName} can buy all courses"

    def readArticles(self):
        return f"{self.userName} can read all articles"

    def getUserBirthDate(self):
        return 2019 - self.userAge