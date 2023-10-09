import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rps_list=[rock, paper, scissors]
print(f"Your chocie: {your_choice} {rps_list[your_choice]}")
computers_choice=random.randint(0,2)
print(f"Computers choice: {computers_choice} {rps_list[computers_choice]}")

if (your_choice >= 3) or (your_choice < 0):
    print("You typed an invalid number, you lose!")
elif (your_choice == 0) and (computers_choice==2):
    print("You win!")
elif (your_choice == 2) and (computers_choice==0):
    print("Computer wins. You lose!")
elif (your_choice == 2) and (computers_choice==1):
    print("You win!")
elif (your_choice == 1) and (computers_choice==0):
    print("You win!")
elif (your_choice == 0) and (computers_choice==1):
    print("Computer wins. You lose!")
elif (your_choice == 1) and (computers_choice==2):
    print("Computer wins. You lose!")
else:
    print("It is a draw!")