board = ['-' for i in range(9)]

def Displayboard():
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")

player1 = "X"
player2 = "O"

def check_conditions(player):
    conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
        [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6],
    ]
    for check in conditions:
        if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
            return 1
    else:
        return 0

def StartGame():
    Displayboard()
    while True:
        while True:
            player1_option = input(f"{player1}, Enter Your Position:")

            if player1_option not in [str(i) for i in range(1, 10)]:
                print("Please Enter [1-9]")
                continue

            if board[int(player1_option) - 1] == "-":
                board[int(player1_option) - 1] = player1
                Displayboard()
                if check_conditions(player1):
                    return f'Winner : {player1}'
                break
            else:
                print("This Place not a Empty!")

        if len([i for i in board if i == '-']) == 0:
            return ' '

        while True:
            player2_option = input(f"{player2}, Enter Your Position:")

            if player2_option not in [str(i) for i in range(1, 10)]:
                print("Please Enter [1-9]")
                continue

            if board[int(player2_option) - 1] == "-":
                board[int(player2_option) - 1] = player2
                Displayboard()
                if check_conditions(player2):
                    return f'Winner : {player2}'
                break
            else:
                print("This Place not a Empty!")

print(StartGame())

while True:
    play_again = input("Do You Want Play Again [y/n]:")
    if play_again in "yY":
        board = ['-' for i in range(9)]
        print(StartGame())
    else:
        exit()
