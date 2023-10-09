print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('''Welcome the treasure island :)
Your mission is find the treasure!''')
crossroad = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if(crossroad == 'left'):
    lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if (lake=='wait'):
        island = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if (island=='yellow'):
            print("You choose the room with full of poisinous snakes. Game over.")
        elif (island=='red'):
            cave = input("You\'ve come to a cave. There are two exits. Type 'one' or 'two'.\n").lower()
            if (cave=='one'):
                chest = input("You've come to a beach. There are three treasure chest. Choose one of them(first, second or third).\n")
                if (chest=='first'):
                    print("You found the treasure! You win!")
                elif (chest=='second'):
                    print("You found rocks in the chest. Game over.")
                else:
                    print("There is nothing in the chest. Game over.")
            else:
                print("You fell into a cliff. Game over.")
        elif (island=='blue'):
            print("You enter a room of beasts. Game Over.")
        else:
            print("You choose the door doesn't exist. Game over!")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
