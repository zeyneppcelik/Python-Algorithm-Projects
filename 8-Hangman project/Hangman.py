import random
import hangman_art
from hangman_word_list import word_list

print(hangman_art.logo)
chosen_word=random.choice(word_list)
word=[]
for i in range(len(chosen_word)):
    word+='_'

lives = 6
while (word.count('_')!=0):
    print(word)
    guess_letter=str(input("Guess a letter: ").lower)

    if guess_letter in word:
        print('You have already guessed this letter.')

    if guess_letter not in chosen_word:
        print(hangman_art.stages[lives])
        print('You lose a life. The letter that you guessed is not in the word.')
        lives-=1
    else:
        for i,j in enumerate(chosen_word):
            if j== guess_letter:
                word[i]=guess_letter
    if lives==0:
        print(hangman_art.stages[lives])
        print('You lose!!')
        break
    
    if '_' not in word:
        print('You win!!')
        print(''.join(word))