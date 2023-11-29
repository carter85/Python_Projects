import random

def play_game():
    num = random.randint(0,51)
    print(num)
    tries = 5
    guess = 0

    #while guess != num:
    while tries > 0:
        guess = int( input('enter number\n') )
        print(tries)
        
        match num:
            case < guess:
                print('too high')
                tries -= 1
            case (guess < num):
                    print('too low')
                    tries -= 1
            case _:
                print('correct')
            
            
    print('out of tries')
    
play_game()

