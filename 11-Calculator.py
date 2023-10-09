import os
def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations={'+':add,
            '-':subtract,
            '*':multiply,
            '/':divide}

print("Welcome to calculator :)")
def calculator():
    print("""
 _____________________
|  _________________  |
| |              0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)
    number1=float(input("What is the first number: "))
    for operation in operations:
        print(operation)
    new_calc=True
    while new_calc:
        chosen_operation=input("Pick an operation: ")
        number2=float(input("What is the second number: "))
        func=operations[chosen_operation]
        answer=func(number1,number2)
        print(f'{number1} {chosen_operation} {number2} = {answer}')
    
        should_cont=input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation or type 'e' to exit: ")
        if should_cont=='y':
            number1=answer
        elif should_cont=='n':
            os.system('cls')
            calculator()
        else:
            new_calc=False

calculator()
print('GOODBYE :)')