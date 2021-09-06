
def display_board():
    global board
    for row in board:
        for col in row:
            print(str(col), end=' ')
        print()
    print("-------------")
    print("0 1 2 3 4 5 6")


def turn(plr):
    global board
    pos = int(input("Choose a location [0 - 6]: "))
    j = 5
    while board[j][pos] != 0 and j > 0:
        j -= 1
    board[j][pos] = plr

board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]


run = True
while run:
    display_board()
    turn(1)
    display_board()
    turn(2)
