'''this is a simple guessing number game where the cumputer will chose
a number and the user need to guess that number'''

import random

def guess():
    #Asking the user to give a starting and an ending point, to guess in between them
    start = int(input("Pleaze give a starting point:  "))
    end = int(input("Pleaze give a ending point:  "))

    #generating a random number
    random_number = random.randint(start, end)

    #while loop that ask the user to guess then give feedback
    while True:
        guess = 0
        
        guess = int(input("Please try if you can guess a number between "+ str(start)+ " and " + str(end)+ ":  "))
        if guess == random_number:
            print("You won!!!! you guess was right.")
            break
        elif guess < random_number:
            print("You're bellow the numbe!!! go up")
        else:
            print("You're above the number!!! go low")

guess()