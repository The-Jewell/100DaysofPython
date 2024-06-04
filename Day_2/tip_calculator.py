#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

#gathering inputs needed 
bill = input("What was the total bill? \n$" )
tip = input("What percentage tip would you like to give? 10, 12, or 15? \n")
people = input("How many people are splitting the bill?\n")

#converting strings to ints/floats
bill_as_float = float(bill)
tip_percent = int(tip) / 100 #converting tip to a percentage 
people_as_int = int(people)

#calculating total bill
total_bill = bill_as_float *(1 +tip_percent)
#calculating total for each person
total_per_person = (total_bill / people_as_int)
#printing out result
print(f"Each person should pay: ${total_per_person:.2f}")