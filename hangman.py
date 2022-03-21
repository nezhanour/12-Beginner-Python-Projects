import random
from unittest import skip
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)  #the word chosen randomly 
    word_letters = set(word)  #letters in the shosen word as a set
    alphabet = set(string.ascii_uppercase)  # uppercase letters in the english dict
    used_letters = set()  #track what user guessed correctly
    lives = 6

    while len(word_letters) > 0 and lives > 0: 
        print ('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
    
        user_letter = input("guess a letter: ").upper() #getting user input
        if user_letter in alphabet - used_letters: #checking if the user guess is in alphabet and haven't been guessed yet then add it to the set of correctly guessed letters
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print ('letter is not in the word')

        elif user_letter in used_letters:
            print("you have already userd that letter. guess again")
        
        else:
            print("Invalid character. try again")
        

    if lives == 0:
        print("you died, sorry. the word was", word)
    else:
        print("Bravo!!!! you guessed the word", word,"correctly!!!")


play = input("Hello to HANGMAN game. Would you like to play. press 'Y' to play and 'N' to quit:"  ).lower()
while True:
    if play == 'y':
        hangman()
        break

    elif play == 'n':
        print("see you next time")
        break
    else:
        #expected behavior get back at the top of the while loop if the user enter a letter other than 'n' or 'y'
        #output keep printing 'invalid option' 
        print("invalid option")
        continue

