# guide on https://codefather.tech/blog/hangman-game-python/

import random, sys, hangman_stages

words = ['fiscal','eggoliant','thriving','concerta','fillicide']

def select_words(words):
    return random.choice(words)

remaining_attempts = 6
guessed_letters = ''

def print_secret_word(secret_word):
    print(' _ ' * len(secret_word))

print('Welcome to Hangman, attempt to guess this word:\n')
secret_word = select_words(words)
print(hangman_stages.get_hangman_stage(remaining_attempts))
print_secret_word(secret_word)

def guess_letter():
    guess = input('Guess a letter: ')
    if len(guess) > 1 or not guess.isalpha():
        print('Only single letters are allowed. Unable to continue...')
        sys.exit()
    return guess.lower()

