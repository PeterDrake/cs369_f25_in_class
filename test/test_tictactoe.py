from tictactoe import *

def test_finds_successor():
    assert successor('O......X.', 'X', 2) == 'O.X....X.'

def test_finds_legal_moves():
    assert legal_moves('O......X.') == [1, 2, 3, 4, 5, 6, 8]

def test_finds_winner():
    assert winner('O.O...XXX') == 'X'

def test_finds_diagonal_winner():
    assert winner('OXOXOX.XO') == 'O'

def test_finds_value_at_end_of_game():
    assert value('XXX...OO.', 'X') == 1

def test_finds_winning_value_at_depth_1():
    assert value('XX....OO.', 'X') == 1

def test_finds_tie_value_at_depth_1():
    assert value('XOXXOXO.O', 'X') == 0

def test_finds_deeper_winning_value():
    assert value('XOXXO.O..', 'X') == 0

def test_finds_best_move_depth_1():
    assert best_move('XOXXO.O.X', 'O') == 7

def test_finds_best_move_depth_2():
    assert best_move('XOXXO.O..', 'X') == 7
