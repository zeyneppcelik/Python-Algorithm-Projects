from Heigher_lower_data import data
import random
import os
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def compare(a,b):
    if a['follower_count']>b['follower_count']:
        return 'A'
    else:
        return 'B'

def random_number():
    number=random.randint(0,len(data)-1)
    return number

count_score=0
end_game=True

A=data[random_number()]
while(end_game):
    
    print(logo)
    
    B=data[random_number()]
    print('Compare A: ' + A['name'] + ' , ' + A['description'] + ' , from '+ A['country'] + str(A['follower_count']))
    print(vs)
    print('Against B: ' + B['name'] + ' , ' + B['description'] + ' , from '+ B['country'] + str(B['follower_count']))

    answer=input("Who has more followers? Type 'A' or 'B':   ")

    comp=compare(A,B)
    if answer==comp:
        if comp=='B':
            A=B
        count_score=count_score+1
        os.system('cls')
    else:
        end_game=False
        print(f"You Lose! Your score: {count_score}")

    