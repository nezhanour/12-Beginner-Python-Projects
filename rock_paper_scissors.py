import random




def game():

    user_win = 0
    computer_win = 0
    ties = 0

    play = input("Let's play rock paper scissors. press 'Y' for yes or 'N' for no:  ").lower()
    if play == 'y':
        while True:
            user = input ("What's your choice 'R' for rock, 'P' for paper, 'S' for scissors, 'Q' for quitting:  " ).lower()
            computer = random.choice(['r', 'p', 's'])

            if user == 'q':
                print(f'the game ends with you winning {user_win} times, the computer winning {computer_win} times, and having {ties} ties. ')
                print("OK!!! Bye") 
                quit()
            
            elif user not in ['r', 'p', 's']:
                print('invalid choice, try again')
                continue

            elif user == computer:
                print(f'computer chose {computer} it\'s tie')
                ties += 1

            elif is_win(user, computer):
                print(f'computer chose {computer} You won!!!')
                user_win += 1

            else:
                print(f'computer chose {computer} you lost')
                computer_win += 1
    else:
        return "goodbye"

    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == "r"):
        return True


print(game())

