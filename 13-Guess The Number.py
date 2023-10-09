import random
print( """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
""")

def remaining_attempt(attempt):
    return attempt -1

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
difficulty=input("Choose a difficulty. For easy type 'e' or hard type 'h': ")
if difficulty=='e':
    attempts=10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty=='h':
    attempts=5
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    print("It is not a valid choise!")

chosen_number=random.randint(1,100)

end_game=True
while end_game:
    guess=int(input("Make a guess: "))
    if guess==chosen_number:
        print(f"You win! The chosen number is {chosen_number}")
        end_game=False
    else: 
        attempts=remaining_attempt(attempts)
        if attempts==0:
            print("You do not have any attempts. You lose!")
            print(f"The chosen number is {chosen_number}")
            end_game=False
        else:
            if guess>chosen_number:
                print("Too high!")
            else:
                print("Too low!")
            print(f"You have {attempts} attempts remaining to guess the number.")
