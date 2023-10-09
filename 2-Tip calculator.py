print("Welcome to tip calculator :)")
total_amount = float(input("What was the total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? (10,12,20)\n"))
number_of_people = int(input("How many people to split the bill?\n"))

total_amount = total_amount + ((total_amount*tip_percentage)/100)
split_amount = total_amount/number_of_people
split_amount = "{:.2f}".format(split_amount)   

print("Each person should pay :"+split_amount) 
