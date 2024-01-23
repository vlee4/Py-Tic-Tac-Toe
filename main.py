print("Hello World")
the_board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

def display_board(board):
  # The function accepts one parameter containing the board's current status
  # and prints it out to the console.
  print(board)


def enter_move(board):
  # The function accepts the board's current status, asks the user about their move,
  # checks the input, and updates the board according to the user's decision.
  return


def make_list_of_free_fields(board):
  # The function browses the board and builds a list of all the free squares;
  # the list consists of tuples, while each tuple is a pair of row and column numbers.
  free_spaces = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      square = board[i][j]
      if square != "X" or square != "O":
        free_spaces.append((i,j))
  return free_spaces


def victory_for(board, sign):
  # The function analyzes the board's status in order to check if
  # the player using 'O's or 'X's has won the game
  return


def draw_move(board):
  # The function draws the computer's move and updates the board.
  return

print("Here's the board", make_list_of_free_fields(the_board))