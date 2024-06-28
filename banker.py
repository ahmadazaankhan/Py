import random

names_string = "This, is the, boy and someone else"
names = names_string.split(",")



num_items = len(names)

# print (num_items)

random_choice = random.randint(0, num_items - 1)

print (names[random_choice])


print(names[random_choice] + " is going, to buy the, meal today!")


names = names_string.split(", ") 




import random

random_name = random.choice(names)

print(f"{random_name} is going to buy the meal today!")