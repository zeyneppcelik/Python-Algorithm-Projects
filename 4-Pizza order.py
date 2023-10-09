print("Welcome!")
size = input("Which size would you like to order your pizza? S, M or L?")

bill=0
if (size == 'S'):
    bill +=15
elif (size == 'M'):
    bill +=20
elif (size == 'L'):
    bill +=25

pepperoni = input("Would you like to add pepperoni? (Y or N)")
if (pepperoni == 'Y'):
    if (size == 'S'):
        bill +=2
    else:
        bill +=3

cheese = input("Would you like to add extra cheese? (Y or N)")
if (cheese == 'Y'):
    bill +=1

print(f"Final bill: {bill}")