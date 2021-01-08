

board = [[0,0,0,0,4,0,0,6,0],
         [0,0,6,1,2,0,3,0,0],
         [0,0,0,0,0,0,0,2,7],
         [0,7,0,6,0,0,0,0,3],
         [0,0,4,0,0,0,5,0,0],
         [2,0,0,0,0,3,0,1,0],
         [5,4,0,0,0,0,0,0,0],
         [0,0,1,0,8,2,6,0,0],
         [0,3,0,0,9,0,0,0,0]]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            print(board[i][j], end="")
        print("")
    print("")

def find_empty(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == 0:
                return (y, x) #row or y, col or x
    return False

#pos for position
def validate(board, num, pos):
    
    #cheacks row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num:
            return False

    #cheacks coulum
    for i in range(len(board[0])):
        if board[i][pos[1]] == num:
            return False

    #cheacks square
    box_x = pos[0] // 3 
    box_y = pos[1] // 3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if board[i][j] == num:
                return False

    #all conditions are valid
    return True

#solves the sudoku board
def solver(board):
    pos = find_empty(board)

    if pos == False:
        return True

    for i in range(1, 10):
        if validate(board, i, pos):
            board[pos[0]][pos[1]] = i
            print_board(board)
            
            if solver(board):
                return True
            else:
                board[pos[0]][pos[1]] = 0
                
    #can't find valid num in this board config      
    return False

solver(board)