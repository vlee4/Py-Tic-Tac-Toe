from random import randrange

print("Hello World")
the_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square_key = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2]
}
global round
round = 1


def display_board(board):
  # The function accepts one parameter containing the board's current status
  # and prints it out to the console.
  print(board)
  return board


def enter_move(board):
  # The function accepts the board's current status, asks the user about their move,
  # checks the input, and updates the board according to the user's decision.
  # letter = input("Please enter your letter: ")
  valid_move = False
  while not valid_move:
    user_move = int(input("Enter your move: "))
    #input is int and is b/t 1-9
    if type(user_move) is int and user_move > 0 and user_move < 10:
      #check if space in board is vacant
      chosen_square = square_key[user_move]
      row = chosen_square[0]
      col = chosen_square[1]
      if board[row][col] != "X" and board[row][col] != "O":
        board[row][col] = "O"
        valid_move = True
  global round
  round += 1
  return board


def make_list_of_free_fields(board):
  # The function browses the board and builds a list of all the free squares;
  # the list consists of tuples, while each tuple is a pair of row and column numbers.
  # print("Board i received", board)
  free_spaces = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      square = board[i][j]
      if square != "X" and square != "O":
        free_spaces.append((i, j))
  return free_spaces


def victory_for(board, sign):
  # The function analyzes the board's status in order to check if
  # the player using 'O's or 'X's has won the game
  return


def draw_move(board):
  global round
  # The function draws the computer's move and updates the board.
  if round == 1:
    board[1][1] = "X"
  else:
    choices = make_list_of_free_fields(board)
    random_choice = randrange(len(choices))
    # print("idx", random_choice, "square location", choices[random_choice])
    row = choices[random_choice][0]
    col = choices[random_choice][1]
    board[row][col] = "X"
  round += 1
  return board


# draw_move(the_board)
# print("Board:", display_board(the_board))
# enter_move(the_board)
# print("Board:", display_board(the_board))
# print("Here's the free spacs", make_list_of_free_fields(the_board))
# draw_move(the_board)
# print("Board:", display_board(the_board))
