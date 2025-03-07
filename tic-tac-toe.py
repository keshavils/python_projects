from random import randrange

def display_board(board):
    for row in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter your move (1-9) : "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9")
                continue

            row = (move-1) // 3
            col = (move-1) % 3

            if board[row][col] in ['O', 'X']:
                print("That field is already occupied! Try again.")
                continue
            
            board[row][col] = "O"
            break
        
        except ValueError:
            print("Please enter a valid number!")
            continue

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    
    #check for diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True

    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
        
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


board = [
    ["1", "2", "3"],
    ["4", "X", "6"],
    ["7", "8", "9"]
]
board[1][1] = 'X'

while True:
    display_board(board)

    #user's move
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("You won!")
        break
    
    #checks if board is full
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Tie!")
        break

    #computer's move
    draw_move(board)
    if victory_for(board, 'X'):
        display_board(board)
        print("Computer won!")
        break
    
    #check if the board is full
    if not make_list_of_free_fields(board):
        display_board(board)
        print("Tie!")
        break

