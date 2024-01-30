from random import randrange

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
global game_status
game_status = None


def display_board(board):
  # The function accepts one parameter containing the board's current status
  # and prints it out to the console.
  print("-------")
  for i in range(len(board)):
    print("|", end="")
    for j in range(len(board[i])):
      print(board[i][j], end="|")
    print("\n")
  print("------- \n \n")
  return


def enter_move(board):
  # The function accepts the board's current status, asks the user about their move,
  # checks the input, and updates the board according to the user's decision.
  valid_move = False
  while not valid_move:
    try:
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
        else:
          print("That space is already taken. Try a different space.")
          continue
      else:
        print("Invalid move. Please inter a number 1-9.")
    except ValueError:
      print("Invalid move. Please inter a number 1-9.")
      continue
  global round
  round += 1
  return board


def make_list_of_free_fields(board):
  # The function browses the board and builds a list of all the free squares;
  # the list consists of tuples, while each tuple is a pair of row and column numbers.
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
  global round

  def check_row(row, sign):
    if board[row][0] == sign and board[row][1] == sign and board[row][
        2] == sign:
      return True
    return False

  def check_col(col, sign):
    if board[0][col] == sign and board[1][col] == sign and board[2][
        col] == sign:
      return True
    return False

  def check_diag(col, sign):
    if col == 0:
      if board[0][col] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][col] == sign and board[1][1] == sign and board[2][0] == sign:
      return True
    return False

  # check first row for any of sign
  for i in range(1):
    for j in range(len(board[i])):
      if board[i][j] == sign and check_col(j, sign):
        return sign
        #then check col
  #check diagonals
  if check_diag(0, sign) or check_diag(2, sign):
    return sign
  # check entire first col for any of sign
  for i in range(2):
    if board[i][0] == sign and check_row(i, sign):
      return sign

  if round > 9:
    return "Tie"
  return None


def draw_move(board):
  # The function draws the computer's move and updates the board.
  global round
  if round == 1:
    board[1][1] = "X"
  else:
    choices = make_list_of_free_fields(board)
    random_choice = randrange(len(choices))
    row = choices[random_choice][0]
    col = choices[random_choice][1]
    board[row][col] = "X"
  round += 1
  return board


# Loop turns until game is over
while game_status is None and round < 10:
  if round % 2 == 1:
    print("Here's the board")
    display_board(the_board)
    print("It's now the Computer's turn")
    draw_move(the_board)
    game_status = victory_for(the_board, "X")

  else:
    print("Here's the board")
    display_board(the_board)
    print("It's now the User's turn")
    enter_move(the_board)
    game_status = victory_for(the_board, "O")

else:
  print("+++++++++++++++++")
  print("Here's the final board:")
  display_board(the_board)
  if game_status == "Tie":
    print("Game over. It's a tie!")
  else:
    print(f"Game over. The winner is: {game_status}")
