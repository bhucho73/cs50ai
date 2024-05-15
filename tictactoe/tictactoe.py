"""
Tic Tac Toe Player
"""
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None
# last_turn = ""

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    """
    if last_turn == "X":
        return O
    else:
        return X
    """
    x_cnt = 0
    o_cnt = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == "X":
                x_cnt = x_cnt + 1
            elif board[x][y] == "O":
                o_cnt = o_cnt + 1
    #print("in player ", o_cnt, x_cnt)
    if o_cnt >= x_cnt:
        return X
    else:
        return O
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # go through all the squares on the board and add EMPTY squares to the set

    actions = set()
    #print("in actions()")
    for x in range(0,3):  # rows
        for y in range(0,3):   #cols
            if board[x][y] == EMPTY:
                actions.add((x,y))
    #print("actions() end")
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    #print("in result ", i, j)

    #if (0 <= action[0] < 3) and (0 <= action[1] < 3) and (board[action[0]][action[1]] == EMPTY):
    if (0 <= i < 3) and (0 <= j < 3) and (board[i][j] == EMPTY):
        copy = deepcopy(board)
        copy[i][j] = player(board)
        #board[i][j] = player(board)
        #if last_turn == "X":
        #    last_turn = "O"
        #else:
        #    last_turn = "X"
    else:
        print("Invalid action. Board not changed!")
    #print(copy)

    return copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #print("in winner", board)
    #print(board[0][2],board[1][2],board[2][2] )
    x = board[0][2]
    y = board[1][2]
    z = board[2][2]
    #if x == y and y == z:
        #return x
    if board[0][0] == board[0][1] == board[0][2]:  #row 1
        return board[0][0]

    if board[1][0] == board[1][1] == board[1][2]:  #row 2
        return board[1][0]

    if board[2][0] == board[2][1] == board[2][2]:  #row 3
        return board[2][0]

    if board[0][0] == board[1][0] == board[2][0]:  #col 1
        return board[0][0]

    if board[0][2] == board[1][2] == board[2][2]:  # col 3
        return board[0][2]

    if board[0][1] == board[1][1] == board[2][1]:  #col 2
        return board[0][1]

    if board[0][0] == board[1][1] == board[2][2]:  #diag 1
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:  #diag 2
        return board[0][2]

    else:
        return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #print("in terminal()")
    #print("winner ", winner(board), board)
    #print("action length ", len(actions(board)))
    if winner(board) == "X" or winner(board) == "O" or len(actions(board)) == 0:
        #print("true", winner(board))
        return True
    else:
        #print("false")
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #print("in util", winner(board))
    if winner(board) == "X":
        #print("in util: Winner: X")
        return 1
    elif winner(board) == "O":
        #print("in util: Winner: O")
        return -1
    else:
        #print("in util: Winner: None")
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #print("in minimax")
    if terminal(board):
        return None  # None or utility?
    p = player(board)
    #print("Player ", p)
    match p:
        case 'X':
            #print("MAX player optimal action...")
            return max_value_move(board)[1]
        case 'O':
            #print("MIN player optimal action...")
            return min_value_move(board)[1]
        case _:
            print("Neither MIN nor MAX player? Returning None")
            return None


def max_value_move(board, best_value=100.0):
    #print("MAX")
    #best_value = float('-inf')
    value = -100.0
    best_move = None
    if terminal(board):
        return utility(board), None
    moves = actions(board)      # Available moves

    for move in moves:
        #print("MAX: ", move, best_move, value, best_value)
        if terminal(board):
            util = utility(result(board, move))
            #print("MAX move: ", util)
            return util, move
        if best_value <= value:
            #value = best_value
            break
            #continue
        #if len(moves) == 1:  # only one move left. Return it
        val, mv = min_value_move(result(board, move), value)
        #print("MAX: val %f, best_value %f", val, mv)
        if val > value:
            value = val
            best_move = move
            #print("MAX: val %f, best_value %f", best_value, best_move)
        #print("MAX END: ", move, best_move, value, best_value)
    return value, best_move


def min_value_move(board, best_value=-100.0):
    #print("MIN")
    #best_value = float('inf')
    value = 100.0
    best_move = None
    if terminal(board):
        return utility(board), None
    moves = actions(board)

    for move in moves:
        #print("MIN: ", move, best_move, value, best_value)
        if terminal(board):
            util = utility(result(board, move))
            #print("MIN move: ", util)
            return util, move
        if best_value >= value:
            #value = best_value
            break
            #continue
        #if len(moves) == 1:         # only one move left. Return it
        val, mv = max_value_move(result(board, move), value)
        #print("MIN: val %f, best_value %f", val, mv)
        if val < value:
            value = val
            best_move = move
            #print("MIN: val %f, best_value %f", best_value, best_move)
        #print("MIN END: ", move, best_move, value, value)
    return value, best_move
