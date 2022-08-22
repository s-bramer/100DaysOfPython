print("Welcome to the tip calculator.\n")
bill = input("What was the total bill £")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

portion = round((float(bill)*(int(tip)/100) + float(bill))/int(people),2)

print(f"Each person should pay: £{portion}")
