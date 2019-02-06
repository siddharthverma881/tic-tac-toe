import os

def display_board():
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("----------")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("----------")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def start_game():
    print("You want to be 'X' or 'O' ? ")
    player_name = input().upper()
    if(player_name == 'X' or player_name == 'O'):
        return player_name
    else:
        print('Enter a valid input')
        os.system('cls')
        start_game()      

def assign_player():
    player1 = start_game()
    if(player1 == 'X'):
        player2 = 'O'
    elif(player1 == 'O'):
        player2 = 'X'
    print('player1 = ' , player1)
    print('player2 = ' , player2)
    return player1

def check_winner(board,player):
    if(player == 'X'):
        playing = 1
    else:
        playing = 2
    value = 0
    if(board[1] == board[2] == board[3]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    elif(board[4] == board[5] == board[6]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    elif(board[7] == board[8] == board[9]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    elif(board[1] == board[4] == board[7]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    elif(board[2] == board[5] == board[8]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    elif(board[3] == board[6] == board[9]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    elif(board[1] == board[5] == board[9]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    elif(board[3] == board[5] == board[7]  == player):
        print("player" , playing , "wins the game")
        value=1
        return value
    return value

def mark_position(board,player1,player2):
    turn = 0
    player_number = 1
    while turn < 9:
        print("Player" , player_number , "its your turn,enter the position " )
        position_string = input()
        position = int(position_string)
        if (player_number == 1):
            board[position] = player1
            player_number = 2
            display_board()
            if(check_winner(board,player1)):
                break
        elif (player_number == 2):
            board[position] = player2
            player_number = 1
            display_board()
            if(check_winner(board,player2)):
                break
        turn = turn + 1

player1 = assign_player()
if(player1 == 'X'):
    player2 = 'O'
elif(player1 == 'O'):
    player2 = 'X'
board = [" "] * 10
display_board()
mark_position(board,player1,player2)