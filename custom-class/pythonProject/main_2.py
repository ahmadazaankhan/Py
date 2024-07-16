class User:

    def __init__(self, user_id, username, follower):
        self.id = user_id
        self.username = username
        self.followers = follower
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "asher", "1M")
user_2 = User("002", "shahzain", "10M")

print(user_1.id)
print(user_2.followers)


# user_2 = User()
# user_2.id = "002"
# user_2.name = "jack"

# class Person:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#
#
# person_1 = Person("003", "hadi")
# person_2 = Person("004", "Zoya")
#
# print(person_1.username)
# print(person_2.id)
