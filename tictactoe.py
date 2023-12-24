import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    x=0
    o=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X': x+=1
            elif board[i][j] == 'O': o+=1
    return O if x>o else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibilities = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY: possibilities.add((i,j))
    return possibilities

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY: raise Exception("That action is not valid")

    resultBoard = copy.deepcopy(board)
    resultBoard[action[0]][action[1]] = player(board)
    return resultBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]

    for i in range(len(board)):
        xhtimes=0
        ohtimes=0
        xvtimes=0
        ovtimes=0

        for j in range(len(board[0])):
            if board[i][j] == 'X': 
                xhtimes+=1
                if xhtimes == 3:
                    return 'X'
            elif board[i][j] == 'O': 
                ohtimes+=1
                if ohtimes == 3:
                    return 'O'
            if board[j][i] == 'X':
                xvtimes+=1
                if xvtimes == 3:
                    return 'X'
            elif board[j][i] == 'O':
                ovtimes+=1 
                if ovtimes == 3:
                    return 'O'
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): return True

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = {
        'X': 1,
        'O': -1,
        None: 0
    }

    return player.get(winner(board))
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    
    return maxValue(board)[1] if player(board) == X else minValue(board)[1]
    
 
def maxValue(board):
    utilityAndAction = [-math.inf, None]
    action = None

    if terminal(board): return [utility(board), None]
    
    for possibility in actions(board):
        aux = utilityAndAction[0]
        
        utilityAndAction[0] = max(utilityAndAction[0], minValue(result(board, possibility))[0])  
        
        if aux != utilityAndAction[0]:
            action = possibility
            if utilityAndAction[0] == 1: return [utilityAndAction[0], action]
   
    return [utilityAndAction[0], action]

def minValue(board):
    utilityAndAction = [math.inf, None]
    action = None
    
    if terminal(board): return [utility(board), None]
   
    for possibility in actions(board):
        aux = utilityAndAction[0];
        
        utilityAndAction[0] = min(utilityAndAction[0], maxValue(result(board, possibility))[0]) 
        
        if utilityAndAction[0] != aux:
            action = possibility
            if utilityAndAction[0] == -1: return [utilityAndAction[0], action]

    return [utilityAndAction[0], action]
