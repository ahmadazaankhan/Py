class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "asher")

print(user_1.id)

# user_2 = User()
# user_2.id = "002"
# user_2.name = "jack"