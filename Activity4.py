import random
playing=True
number=str(random.randint(10,20))
print("I have generated a number from 10 to 19,You have to guess the number")
print("The game ends when you guess the correct number")
while playing:
    guess=input("Make a guess. \n")
    if number == guess:
        print("You win")
        print("The number was",number)
        break
    else:
        print("You loose. \n")