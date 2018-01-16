board = []

#make a 5 x 5 board
for i in range(5):
    board.append([])
    for j in range(5):
        board[i].append("O")

#display the board
def print_board(board_in):
  for i in range(len(board_in)):
    print " ".join(board_in[i])

print_board(board)

#randomly place game pieces on board
from random import randint
def random_row(board_in):
  return randint(0, len(board_in)-1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#play the game
for turn in range(4):
    print "Turn %i" %(turn + 1)
    #obtain guess from player (correct for index)
    guess_row = int(raw_input("Guess Row (1- 5): ")) -1
    guess_col = int(raw_input("Guess Column (1- 5): ")) -1

    #check if the player hit or not, and mark a miss
    if guess_row == ship_row and guess_col == ship_col:
        print "You sunk my battleship, those poor souls"
        break
    else:
        if guess_row not in range(len(board)) or guess_col not in range(len(board[0])):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
    print_board(board)
