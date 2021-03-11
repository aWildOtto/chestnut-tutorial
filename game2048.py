from utilities import generate_piece, print_board

DEV_MODE = False


def add_left(board: [[int, ], ]):
    changed = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                current_value = board[i][j]
                # loop through the remaining block in the row
                for k in range(j+1, len(board[i])):
                    if board[i][k] != board[i][j] and board[i][k] != 0:
                        break
                    if current_value == board[i][k]:
                        board[i][j] = current_value * 2
                        board[i][k] = 0
                        changed = True
    return board, changed


def add_down(board: [[int, ], ]):
    changed = False
    for i in reversed(range(len(board))):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                current_value = board[i][j]
                # loop through the remaining block in the row
                for k in range(i-1, -1, -1):
                    if board[k][j] != board[i][j] and board[k][j] != 0:
                        break
                    if current_value == board[k][j]:
                        board[i][j] = current_value * 2
                        board[k][j] = 0
                        changed = True

    return board, changed
    
    
def add_right(board: [[int, ], ]):
    changed = False
    for i in range(len(board)):
        for j in reversed(range(len(board[i]))):
            if board[i][j] != 0:
                current_value = board[i][j]
                # loop through the remaining block in the row
                for k in range(j-1, -1, -1):
                    if board[i][k] != board[i][j] and board[i][k] != 0:
                        break
                    if current_value == board[i][k]:
                        board[i][j] = current_value * 2
                        board[i][k] = 0
                        changed = True
    return board, changed
    

def add_up(board: [[int, ], ]):
    changed = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                current_value = board[i][j]
                # loop through the remaining block in the row
                for k in range(i+1, len(board)):
                    if board[k][j] != board[i][j] and board[k][j] != 0:
                        break
                    if current_value == board[k][j]:
                        board[i][j] = current_value * 2
                        board[k][j] = 0
                        changed = True

    return board, changed


def shift(board: [[int, ], ], direction):
    new_board = [] 
    # with all cells empty 
    for i in range(4): 
        new_board.append([0] * 4) 

    row_list = range(len(board))

    if direction in ['s', 'd']:
        row_list = reversed(row_list)
    for i in row_list: 
        pos = 0
        col_list = range(len(board[i]))
        if direction in ['s', 'd']:
            pos = len(board) - 1
            col_list = reversed(col_list)  
        for j in col_list: 
            if direction == 'w': #up
                if(board[j][i] != 0): 
                    new_board[pos][i] = board[j][i] 
                    pos += 1

            if direction == 'a': #left
                if(board[i][j] != 0): 
                    new_board[i][pos] = board[i][j] 
                    pos += 1
        
            if direction == 's': #down
                if(board[j][i] != 0): 
                    new_board[pos][i] = board[j][i] 
                    pos -= 1
        
            if direction == 'd': #right
                if(board[i][j] != 0): 
                    new_board[i][pos] = board[i][j] 
                    pos -= 1
    
    return new_board, new_board != board


def add_block(game_board):
    new_piece = generate_piece(game_board, DEV_MODE)
    game_board[new_piece['row']][new_piece['column']] = new_piece['value']


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    add_block(game_board)
    add_block(game_board)

    print_board(game_board)
    gameRunning = True

    for i in range(4):
        if 2048 in game_board[i]:
            gameRunning = False

    if game_over(game_board):
        gameRunning = False

    while gameRunning:
        move = input()
        move = move.lower()
        move_list = ['w', 'a', 's', 'd']
        changed = False
        if move in move_list:
            # 3 update board
            if move == 'w':
                game_board, changed = add_up(game_board)
            if move == 's':
                game_board, changed = add_down(game_board)
            if move == 'a':
                game_board, changed = add_left(game_board)
            if move == 'd':
                game_board, changed = add_right(game_board)
     
            game_board, shifted = shift(game_board, move)

            if changed or shifted:
                add_block(game_board)
                print_board(game_board)
        
            for i in range(4):
                if 2048 in game_board[i]:
                    gameRunning = False

            if game_over(game_board):
                gameRunning = False

        if move == 'q':
            print('Good bye')
            gameRunning = False
            
    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    zero_counter = 0
    has_duplicate = False
    for i in range(4):
        for j in range(4):
            if game_board[i][j] == 0:
                zero_counter += 1

            else:
                if j < 3 and i < 3:
                    if game_board[i][j] == game_board[i][j+1] or game_board[i][j] == game_board[i+1][j]:
                        has_duplicate = True
                elif i < 3:
                    if game_board[i][j] == game_board[i+1][j]:
                        has_duplicate = True
                elif j < 3:
                    if game_board[i][j] == game_board[i][j+1]:
                        has_duplicate = True

    return zero_counter == 0 and not has_duplicate

if __name__ == "__main__":

    init_board = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
    board = main(init_board)
