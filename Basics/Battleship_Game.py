# [Python random module](https://docs.python.org/3/library/random.html)
# import the module that allows you to work with random numbers []()
from random import randint

# Define your border as empty
board = []

# Initialize your board fully with "O character
for x in range(5): # You can change your board size
  board.append(["O"] * 5)

# Runs through board prints elements seperated by a "space"
def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

# Initialize your ship's row number
def random_row(board):
  return randint(0, len(board) - 1)

# Initialize your ship's col number
def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# print(ship_row)
# print(ship_col)

for turn in range(4):
  # the lines that take your guesses for the coordinates of target ship
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if (guess_row == ship_row and guess_col == ship_col): # if your guess is correct it finishes the game
    print("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): # Checks if we gave a valid coordinate
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
  if((3-turn)!=0):
      print("Your remaining guesses is below")  
      print(3-turn)
  print_board(board)
  if(turn==3):
    print("Game Over")