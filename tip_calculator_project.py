#tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
#print(tip_percent)
tip_pay = 1 + tip_percent
print(tip_pay)
split_bill = bill * tip_pay
#print(split_bill)
each_pay = split_bill / people
#print(each_pay)
round_pay = round(each_pay, ndigits=2)
#print(round_pay)
print("Each person should pay: $" + str(round_pay))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
