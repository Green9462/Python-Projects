import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from list (words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You Have', lives, 'Lives Left and You Have Used These Letters: ', ' '.join(used_letters))

        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Guess a Letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You Have Already Guessed That Character! Please Try Again.')

        else:
            print('Invalid Character. Please try again')

    if lives == 0:
        print('You DIED, Sorry. The Word was', word)
    else:
        print('You Guessed The Word', word, '!!')



hangman()









