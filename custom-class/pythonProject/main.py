class User:

    def __init__(self, user_id):
        self.id = user_id

user_1 = User()
user_1.id = "001"
user_1.username = "asher"
user_1.password = "asher"

# print(user_1.password)

user_2 = User()
user_2.id = "002"
user_2.username = "hadi"
user_2.password = "hadi"

user_3 = User()
user_3.id = "003"
user_3.username = "shahzain"
user_3.password = "shahzain"


class Person:

    def __init__(self):
        print("New user is being created")


person_1 = Person()
person_1.id = "003"
person_1.username = "ahmadazaankhan"

# print(person_1.username)

person_2 = Person()
person_2.id = "004"
person_2.username = "zoya"

# print(person_2.username)

"""Initialize
1. to set (variables, counters, switches, etc.) to their starting values at the beginning of a program or subprogram
2. to clear (internal memory, a disk, etc.) of previous data in preparation for use."""

# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#
#         my_car = Car(5)
#         print(my_car)