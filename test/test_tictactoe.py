from tictactoe import *

def test_finds_successor():
    assert successor('O......X.', 'X', 2) == 'O.X....X.'

def test_finds_legal_moves():
    assert legal_moves('O......X.') == [1, 2, 3, 4, 5, 6, 8]

def test_finds_winner():
    assert winner('O.O...XXX') == 'X'

def test_finds_diagonal_winner():
    assert winner('OXOXOX.XO') == 'O'