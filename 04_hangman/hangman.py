# this was being done so bad and wasn't working, gave up and looked up better code

# 23-11-30 Finished 'hangman_better.py' after failing with this one, this gives me angina

from hangman_better import *

# with 'enumerate', word[0] gives integer, word[1] gives value

word_to_guess = 'hangmix'      # make it so user input becomes the word to guess
letter_list = []               # assigned letters from 'word_to_guess' to this list, to check against 'blank_list'
blank_list = []                # list of '_' equal to number of letters in 'word_to_guess'. The working list
letter_guess = 'g'              # letter from user input to check against word
guess_list = []                # list of letters the user has guessed
blank_word = ''                # 'blank_list' gets turned into this string to present to user

# takes word_to_guess length and creates string of blanks _
#   make_blanks(word_to_guess) # this works fine
# 🟢
def make_blanks(word_to_guess):  
    blank_word = ''
    for x in range(len(word_to_guess)):
        #blank_word += ' _ '
        blank_list.append(' _ ')
    print(f'{blank_list}\n{blank_word}')
    return blank_word

# creates list of characters from word_to_guess
# 🟢
def make_letter_list(word_to_guess):  
    letter_list = []
    for x in range(len(word_to_guess)):
        letter_list.append(word_to_guess[x])
    #print(letter_list)
    return letter_list

# takes 'word_to_guess' and 'letter_guess', compares them
# 🟡
def check_letter(letter_list,letter_guess):
    letter_list = make_letter_list(word_to_guess)
    counter = 5
    print('test 4')
    blanks = make_blanks(word_to_guess)

    while counter > 0:
        print(f'counter is {counter}')
        
        print(f'test 3 {blank_list}')
        print(f'test 5 {letter_guess}')
        for index,value in enumerate(letter_list):
            print(f'index is {index}:value is {value}')
            letter_guess = user_guess()
            
            if letter_list[index] != letter_guess:
                print(f'test 1 {letter_guess} is not in word.')
                #print(blank_list)
                
                break
            
            else:
                print(f'test 2 {letter_guess} is in word.')
                blank_list[index] = letter_list[index]
                break
    counter -= 1
    




check_letter(letter_list,letter_guess)

# runs 'create_blank_list()' and 'make_letter_list', assigns
# values to variables
def play_game(word):    
    letter_guess = input('Type letter to guess:\n')
    print(f'You guessed {letter_guess}.')
    prior_guesses = []
    print(f'prior_guesses = {prior_guesses}')
    word = word         
    print(f'word = {word}')
    blanks = make_blanks(word_to_guess)
    print(f'blanks = {blanks}')
    letter_list = make_letter_list(word)
    print(f'make_letter_list = {letter_list}')
    
    check_letter(word,letter_guess)

    # take 'letter_guess', loop through 'letter_list"
    # if found, changes index value in 'blanks'
    # if not, adds to counter, adds value to 'prior_guesses'


"""

        for x in range(len(letter_list)):    

            if letter_list[x] == letter_guess:
                print(f'{letter_guess} is in word.')
                print(f'x is {x}')
                print(blanks[x])
                blanks[x] = letter_guess
                break

            else:   
                print(f'{letter_guess} is not in word.')
                
                continue
"""