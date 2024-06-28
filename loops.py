# For Loops

# for item in list_of_item:
# Do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
# Indentation is imp in python
print(fruits)


# range fucntion

# for number in range(1, 11):
#   print(number)

# for number in range(1, 11, 3):
#   print(number)


total = 0
for number in range (1, 101):
  total += number
print(total)