# INITIAL_STATE
# successor
# legal_moves
# winner
# minimax
# best_move

INITIAL_STATE = '.........'

def successor(state, player, index):
    return state[:index] + player + state[index+1:]

def legal_moves(state):
    return [i for i in range(9) if state[i] == '.']

def winner(state):
    rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]]
    for a, b, c in rows:
        if (state[a] != '.') and (state[a] == state[b] == state[c]):
            return state[a]
    return '.'
