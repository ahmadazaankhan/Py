

import re

def string(number_string):

    value = re.split(r'\d+', number_string)

    value = [value for value in value if value]

    first_name = value[0]
    last_name = value[1]
    id = value[2]

    dictionary = {"first_name": first_name, "last_name": last_name, "id": id}

    return dictionary

number_string = input("Write your name? ")
final_output = string(number_string)
print(final_output)