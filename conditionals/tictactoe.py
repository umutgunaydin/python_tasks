"""
Write a function named tictactoe that determines the outcome of the game in a given tic-tac-toe board.

The dimensions of the board is fixed and equal to three
The board is given as a list of strings
Each element of the list is a string containing three characters: 'X', 'O' or '-'
The function should return 'X', 'O' or 'tie' depending on the outcome of the game
If there are three consecutive 'X's vertically or horizontally 'X' wins the game
If there are three consecutive 'O's vertically or horizontally 'O' wins the game
Otherwise the result is a 'tie'
Note that there will be no case where both players win
"""


def tictactoe(lis):
    if "XXX" in lis:
        return "X"
    elif "OOO" in lis:
        return "O"
    elif (lis[0][0] == "X" and lis[1][0] == "X" and lis[2][0] == "X") or (
            lis[0][1] == "X" and lis[1][1] == "X" and lis[2][1] == "X") or (
            lis[0][2] == "X" and lis[1][2] == "X" and lis[2][2] == "X"):
        return "X"
    elif (lis[0][0] == "O" and lis[1][0] == "O" and lis[2][0] == "O") or (
            lis[0][1] == "O" and lis[1][1] == "O" and lis[2][1] == "O") or (
            lis[0][2] == "O" and lis[1][2] == "O" and lis[2][2] == "O"):
        return "O"
    else:
        return "tie"


print(tictactoe(['XOO', 'XOX', 'XXO']))
print(tictactoe(['XOX', 'OOX', 'XXO']))
print(tictactoe(['XOO', 'XOO', 'OXO']))
