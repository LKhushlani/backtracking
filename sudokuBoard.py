board = [

    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(board):

    find = isEmpty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if isValid(board, i, (row,col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


def printBoard(board):

    for i in range(len(board)):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('|', end = '')

            print(board[i][j]," ", end = "")

        print(" ")

def isValid(board, num, postion):

    #[0,2]
    #check row
    for i in range(len(board[0])):
        if board[postion[0]][i] == num and postion[1] != i:
            return False

    #check col
    for i in range(len(board)):
        if board[i][postion[1]] == num and postion[0] != i:
            return False

    #check block
    box_x = postion[0] // 3
    box_y = postion[1] // 3
    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if board[i][j] == num and (i,j) != postion:
                return False
    return True

def isEmpty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

    return None

print(printBoard(board))
print("-------------------------------")
solve(board)
printBoard(board)





