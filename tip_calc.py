print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))
# bill_w_tip = bill * (1 + int(tip) / 100)
# bill_w_tip = int(tip) / 100 * bill + bill
# print(bill_w_tip)
tip_as_perc = int(tip) / 100
total_tip = bill * tip_as_perc
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
