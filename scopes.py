################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength)

# The other potion strength function is not accessible as it is defined within the function. 
# When you create a new variable or indeed a new function inside another function, it is only accessible within that function. You can only use it when you are inside that function because it has local scope. It is only valid within the walls of the drink_potion function.


# Global Scope
# If we want to use a variable that is defined outside of a function, we have to use the global keyword. The diff b/w global and local scope is where you define or where you create your variable. It could be avaible anywhere bec it is defined at the top level of the file.
# Namespace is the name given to a variable. 

# player_health = 10  <- Global Variable

# def game()
#   def drink_potion():
#     potion_strength = 2 <- Local Variable
#     print(player_health)
    
#   drink_potion()

# print(player_health)

# There is no block scope in python

# if 3 > 2:
#   a_variable = 10


# game_level = 3
# def create_enemy
#   enemies = ["Skeleton", "Zombie", "Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]

#   print(new_enemy)


# # -> How to Modify Varaiable with Global Scope
# enemies = "Skeleton"

# def increase_enemies():
#   enemies += 1
#   print(f" Enemies inside function: {enemies}")

# increase_enemies()
# print(f" Enemies outside function: {enemies}")

# game_level = 3
# def create_enemy():
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#   new_enemy = enemies[0]

# print(new_enemy)

# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton", "Zombie", "Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]

#   print(new_enemy)

# Modifying Global Scopes

enemies = 1
# ^ Variable which has a global scope

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")
# Func which creates a local scope

increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants
# Global scopes could be vv useful especially when you are defining constants. Global constants are variables that you define and you're never planning on changing it ever again. for ex value of pi. Naming convention in python is to write all the alphabets in uppercase. 

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
