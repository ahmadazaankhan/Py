# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formatted_lane = l_name.title()
#     return 



# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format_name("angela", "ANGELA")

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# # formated_string = format_name("AnGELAA", "ATY")
# print(format_name("ANGELa", "YuU"))


def name_format(g_name, r_name):
    if g_name == "" or r_name == "":
        return "You didn't provide valid inputs. "
    # if g_name == "" or r_name == "":

    formated_g_name = g_name.title()
    formated_r_name = r_name.title()
    return f"Result: {formated_g_name} {formated_r_name}"


print(name_format(input("What is your name? "), input("What is your last name? ")))