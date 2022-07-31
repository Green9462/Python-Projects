import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess A Number Between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, Guess Again. Too Low.')
        elif guess > random_number:
            print('Sorry, Guess Again. Too High')


    print(f'Yay, You Have Guessed the Number {random_number} Correctly!')

guess(10)