#BUG - An error in a program that prevents the program from running as expected

# FUNCTION - A piece of code that you can easily call over and over again

# Loop - The action of doing something over and over again

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}

list [2,3,4,5,6,7,8,9,10]

# Retreieving items from dictionary.
print(programming_dictionary["Function"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

# Loop thru a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])