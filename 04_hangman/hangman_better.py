import random, sys, hangman_stages

# Function to choose random word from "words"
def select_word(words):
    return random.choice(words)

# Function to print blank lines for letters in "secret_word"
# Checks to see if letter guessed is in "secret_word", if it 
# is then print the letter in place of a blank line, else it 
# prints a blank line
def print_secret_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(" {} ".format(letter), end="")
        else:
            
            print(" _ ", end="")
    print("\n")

# Takes input from user, if input is not single character or
# not a letter, prints error message and quits
# else it checks guessed letter against "secret_word", returns
# "True" or "False"
def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print('Only single letters are allowed. Unable to continue...')
        sys.exit()
    else:
        if guess in secret_word:
            return True
        else:
            return False

def get_unique_letters(word):
    return ''.join(set(word))

# Word bank to pull from
words = ["tiger", "tree", "underground", "giraffe", "chair"]

# Variables to keep track of game progress
remaining_attempts = 6
guessed_letters = ''

# Prints intro to game, asks for letter to be guessed
print('Welcome to Hangman, attempt to guess this word:\n')
secret_word = select_word(words)



while remaining_attempts > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)):
    guess = input("Guess a letter: ")
    guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)    

    if guess_in_secret_word:
        if guess in guessed_letters:
            print('You have already guessed the letter {}.'.format(guess))
        else:
            print('Yes, the letter {} is part of the secret word.'.format(guess))
            guessed_letters += guess
    else:
        print('No, the letter {} is not part of the secret word.'.format(guess))
        remaining_attempts -= 1

    print(hangman_stages.get_hangman_stage(remaining_attempts))
    print('\n{} attempts remaining\n'.format(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)
    print('\n\nNumber of letters guessed: {}\n'.format(len(guessed_letters)))

if len(guessed_letters) == len(get_unique_letters(secret_word)):
    print('+++ Well done, you won the game +++\n')
else:
    print('--- You have run out of chances ---')

# guide on https://codefather.tech/blog/hangman-game-python/
