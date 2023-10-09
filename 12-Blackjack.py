import random
print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

def compare_scores(scores):
    if scores[1]==0:
        print("Computer Wins With a Blackjack!!")
    elif scores[0]==0:
        print("You Win With a Blackjack!!")
    elif scores[0]>21:
        print("You Went Over, Computer Wins!!")
    elif scores[1]>21:
        print("Computer Went Over, You Win!!")
    elif scores[0]>scores[1]:
        print("You Win!!")
    elif scores[0]==scores[1]:
        print("Draw!!")
    else:
        print("Computer Wins!!")


def calculate_score(player, computer):
    player_score=sum(player)
    computer_score=sum(computer)
    #blackjack control
    if len(player)==2 or len(computer)==2:
        if player==[10,11] or player==[11,10]:
            return 0,computer_score
        elif computer==[10,11] or computer==[11,10]:
            return player_score,0

    if player_score>21:
        if 11 in player:
            player.remove(11)
            player.append(1)
            player_score=sum(player)
    if computer_score>21:
        if 11 in computer:
            computer.remove(11)
            computer.append(1)
            computer_score=sum(dealer)

    return player_score,computer_score

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card=random.choice(cards)
    return random_card

user_cards = []
computer_cards = []
for i in range(0,2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())

is_game_over=False
while not is_game_over:
    scores=calculate_score(player=user_cards, computer=computer_cards)

    if (0 in scores) or (scores[0]>21) or (scores[1]>21):
        print("Game over!")
        is_game_over=True
    else :
        print(f'Your cards: {user_cards} and your current score: {scores[0]}')
        print(f"Computers first card: {computer_cards[0]}")
        continue_game=input("Do you want to draw a card? type 'y' to yes or 'n' to no: ")
        if continue_game=='y':
            user_cards.append(deal_card())
        elif continue_game=='n':
            if scores[1]<17:
                while scores[1]<17 and scores[1]!=0:
                    computer_cards.append(deal_card())
                    scores=calculate_score(player=user_cards, computer=computer_cards)
                is_game_over=True
            else:
                is_game_over=True



print(f'Your cards: {user_cards} and your score: {scores[0]}')
print(f"Computers cards: {computer_cards} and computers score: {scores[1]}")
compare_scores(scores)