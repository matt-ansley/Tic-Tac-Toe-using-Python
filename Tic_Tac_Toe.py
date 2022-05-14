# --- Global Variables ---
#   board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
# If game is still going
game_still_going = True

#Who won? Or tie?
winner = None

# Who's turn is it?
global current_player
current_player = 'X'


# display board
def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def play_game():
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()



    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    if check_if_tie():
        print('Tie!')


def handle_turn(player):
    valid = False
    print(player + "'s turn.")

    position = input("Choose a position 1-9: ")
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Choose a position 1-9: ")

        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print('You can\'t go there. go again')


    board[position] = player
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    #check rows
    check_rows()

    #check columns
    check_columns()

    #check diagonal
    check_diagonals()
    return

def check_for_winner():
    global game_still_going
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    col_winner = check_columns()

    # check diagonals
    diag_winner = check_diagonals()



    if row_winner:
        winner = row_winner()
    elif col_winner:
        winner = col_winner()
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None
        game_still_going = True
    return



def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8]
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    else:
        game_still_going = True
    return

def check_columns():
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'

    global game_still_going
    if col_1:
        print(current_player + ' won!')
        game_still_going = False
    if col_2:
        print(current_player + ' won!')
        game_still_going = False
    if col_3:
        print(current_player + ' won!')
        game_still_going = False
    else:
        game_still_going = True

def check_diagonals():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != '-'
    diag_2 = board[2] == board[4] == board[6] != '-'
    if diag_1:
        print(current_player + ' won!')
        game_still_going = False
    if diag_2:
        print(current_player + ' won!')
        game_still_going = False


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # global variables I need
    global current_player
    if current_player == 'X' :
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return






play_game()