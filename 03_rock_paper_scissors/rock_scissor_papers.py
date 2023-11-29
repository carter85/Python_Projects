import random

def comp_choice():
    rand_num = random.randint(0,2)
    if rand_num == 0:
        return 'Rock'
    elif rand_num == 1:
        return 'Paper'
    else:
        return 'Scissors'
    
def player_choice():
    choice = input( 'Choose: Rock, Paper, Scissors?\n' ).upper()
    if choice == 'Rock' or 'R':
        return 'Rock'
    elif choice == 'Paper' or 'P':
        return 'Paper'
    else:
        return 'Scissors'
    
def compare(comp,player):
    if player == 'Rock' and comp == 'Rock' or player == 'Paper' and comp == 'Paper' or player == 'Scissors' and comp == 'Scissors':
        return 'Tie game.'
    elif player == 'Rock' and comp == 'Scissors' or player == 'Paper' and comp == 'Rock' or player == 'Scissors' and comp == 'Paper':
        return 'Player wins'
    else:
        return 'Player loses'

def round():
    player = player_choice()
    comp = comp_choice()
    result = compare(comp,player)
    
    print('Player chose: ' + player)
    print('Computer chose: ' + comp)
    
    return result

def game():
    i = 5
    comp_wins = 0
    player_wins = 0
    print( 'Rocks, Scissors, Paper, best out of 5:\n')

    while i > 0 :
        winner = round()
        
        if winner == 'Player wins':
            player_wins += 1
            i -= 1
            
        elif winner == 'Player loses':
            comp_wins += 1
            i -= 1
            
        else:
            pass

        print( 'Scoreboard: Player: ' + str(player_wins) + ' ' + 'Computer: ' + str(comp_wins))

    if comp_wins > player_wins:
        print('Computer wins.')
    else:
        print('Player wins.')

game()