from Toplearn.UserModule import User

mohammad = User('sara', 'moradi', 24, 'moh96ordo@gmail.com', '123456')

aliReze = User()

print(f"{mohammad.userName} {mohammad.userFamily} {mohammad.userAge}")
print(f"{aliReze.userName} {aliReze.userFamily} {aliReze.userAge}")

print(mohammad.buyCourse())
print(mohammad.readArticles())

print(mohammad.getUserBirthDate())