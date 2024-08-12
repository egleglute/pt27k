import random
from game_board import start_game
start_game1 = start_game()
def play():
  question = str.capitalize(input("Are you X or O? "))
  if question == "X":
    player = "X"
    computer_is = "O"
  elif question != "X" or "O":
    print("You will be O then! ")
    player = "O"
    computer_is = "X"
  else:
    player = "O"
    computer_is = "X"


  possible_numbers = [1,2,3,4,5,6,7,8,9]
  game_board = [[1,2,3], [4,5,6], [7,8,9]]
  rows = 3
  columns = 3

  # lenta
  def print_game_board():
    for x in range(rows):
      print("\n------------")
      print("|", end="")
      for y in range(columns):
        print("", game_board[x][y], end=" |")
    print("\n------------")
  # zingsniai
  def modify_list(num, turn):
    num = num - 1
    if(num == 0):
      game_board[0][0] = turn
    elif(num == 1):
      game_board[0][1] = turn
    elif(num == 2):
      game_board[0][2] = turn
    elif(num == 3):
      game_board[1][0] = turn
    elif(num == 4):
      game_board[1][1] = turn
    elif(num == 5):
      game_board[1][2] = turn
    elif(num == 6):
      game_board[2][0] = turn
    elif(num == 7):
      game_board[2][1] = turn
    elif(num == 8):
      game_board[2][2] = turn

  # laimetojas
  def check_for_winner(game_board):
    # X asis
    if(game_board[0][0] == 'X' and game_board[0][1] == 'X' and game_board[0][2] == 'X'):
      print("X has won!")
      return "X"
    elif(game_board[0][0] == 'O' and game_board[0][1] == 'O' and game_board[0][2] == 'O'):
      print("O has won!")
      return "O"
    elif(game_board[1][0] == 'X' and game_board[1][1] == 'X' and game_board[1][2] == 'X'):
      print("X has won!")
      return "X"
    elif(game_board[1][0] == 'O' and game_board[1][1] == 'O' and game_board[1][2] == 'O'):
      print("O has won!")
      return "O"
    elif(game_board[2][0] == 'X' and game_board[2][1] == 'X' and game_board[2][2] == 'X'):
      print("X has won!")
      return "X"
    elif(game_board[2][0] == 'O' and game_board[2][1] == 'O' and game_board[2][2] == 'O'):
      print("O has won!")
      return "O"
  #  Y asis
    if(game_board[0][0] == 'X' and game_board[1][0] == 'X' and game_board[2][0] == 'X'):
      print("X has won!")
      return "X"
    elif(game_board[0][0] == 'O' and game_board[1][0] == 'O' and game_board[2][0] == 'O'):
      print("O has won!")
      return "O"
    elif(game_board[0][1] == 'X' and game_board[1][1] == 'X' and game_board[2][1] == 'X'):
      print("X has won!")
      return "X"
    elif(game_board[0][1] == 'O' and game_board[1][1] == 'O' and game_board[2][1] == 'O'):
      print("O has won!")
      return "O"
    elif(game_board[0][2] == 'X' and game_board[1][2] == 'X' and game_board[2][2] == 'X'):
      print("X has won!")
      return "X"
    elif(game_board[0][2] == 'O' and game_board[1][2] == 'O' and game_board[2][2] == 'O'):
      print("O has won!")
      return "O"
  # istryzai
    elif(game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X'):
      print("X has won!")
      return "X"
    elif(game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O'):
      print("O has won!")  
      return "O"
    elif(game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X'):
      print("X has won!")  
      return "X"
    elif(game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O'):
      print("O has won!") 
      return "O" 
    else:
      return "Game failed!"


  turn_counter = 0

  while True:
    # Zaidejo eile
    if(turn_counter % 2 == 0):
      print_game_board()
      number_picked = int(input("\nChoose a number [1-9]: "))
      if(number_picked >= 1 or number_picked <= 9):
        modify_list(number_picked, player)
        possible_numbers.remove(number_picked)
      else:
        print("Invalid input. Please try again.")
      turn_counter = turn_counter + 1
    # Computerio eile
    else:
      while(True):
        cpu_choice = random.choice(possible_numbers)
        print(f"Computer's choice: {cpu_choice}")
        modify_list(cpu_choice, computer_is)
        possible_numbers.remove(cpu_choice)
        print(f"Your possible choices are: {possible_numbers}")
        turn_counter = turn_counter + 1
        break
    
    winner = check_for_winner(game_board)
    if(winner != "Game failed!"):
      print("\nGame over!")
      break
play()
again = input("Would you like to play again? (1-Yes, 2-No): ")
if again == "1":
  play()
else:
  print("Bye!")

    
      