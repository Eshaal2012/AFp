import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input('Enter rock, paper, or scissors: ').lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return

    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print('You win!')
    else:
        print('You lose!')

rock_paper_scissors()