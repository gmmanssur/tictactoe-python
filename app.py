board = [" "," "," ",
        " "," "," ",
        " "," "," "]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2],)
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5],)
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8],)
    print()

def verify_draw():
    show_board()
    print("Draw!")
    return " " not in board

def get_combinations():
    return [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

def verify_winner():
    combinations = get_combinations()
    
    for position1, position2, position3 in combinations:
        x = board[position1]
        y = board[position2]
        z = board[position3]

        if x == y == z and x not in ("", " ", None):
            show_board()
            print("Player ", player, "Won!")
            return True
    
    return False

player = "X"

while True:
    show_board()

    position = input("Choice a position (1-9): ")
    
    if position in ("", " ", None) or not position.isdigit():
        print("Choice a valid position!")
        continue

    position -= 1

    if(board[position] != " "):
        print("This square already occupied! Choice another one.")
        continue

    if position < 0 or position > 8:
        print("Choice a valid position!")
        continue

    board[position] = player

    if(verify_winner() or verify_draw()):
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
