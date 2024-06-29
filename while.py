print("Hello")
num_char = len("Hello")
print(num_char)

def my_function ():
  print("Hello")
  print("Bye")

my_function()


# Reeborg

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
  jump()