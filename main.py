

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
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return (y, x) #row or y, col or x

#pos for position
def validate(board, num, pos):
    
    #cheacks row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[0] != i:
            return False

    #cheacks coulum
    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    #cheacks square
    box_x = pos[0] // 3 
    box_y = pos[1] // 3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if board[i][j] == num and (pos[0] != i or pos[1] != j):
                return False

    #all conditions are valid
    return True