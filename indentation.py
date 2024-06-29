# Indentation is very important in fucntion, it would be shifted to the right by four spaces like this:

def my_function():
    print("Hello")
    print("World")

# It would be inside this function

def my_func():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("Hello")

# LOOPS

# For
for item in list_of_items:
    # Do smth to each item


for number in range(a, b):
    print(number)

# While
while something_is_true:
# 

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -=1
    print(number_of_hurdles)

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

while not at_goal():
    jump()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

