# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 3

# PEMDAS Rule
# Parantheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

# print(3 * 3 + 3 / 3 - 3)

# height = input()
# weight = input()
# weight_int = int(weight)
# height_float = float(height)
# bmi = weight_int / height_float ** 2
# bmi_int = int(bmi)
# print(bmi_int)

height = input()
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)
