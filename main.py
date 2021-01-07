

board = [[2,0,0,7,6,9,5,0,0],
         [6,0,0,0,3,1,2,0,7],
         [0,0,0,2,0,0,0,6,0],
         [1,0,0,0,2,8,0,0,4],
         [8,3,0,0,0,0,0,2,5],
         [4,0,0,5,1,0,0,0,9],
         [0,8,0,0,0,3,0,0,0],
         [7,0,1,8,4,0,0,0,3],
         [0,0,9,6,5,7,0,0,2]]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            print(board[i][j], end="")
        print("")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

