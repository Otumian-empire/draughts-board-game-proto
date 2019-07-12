# display board (grid)
# the grid is a 3 x 3 grid
# any vertex of the grid is a position
# a position has x-index and y-index
grid = [
    [".", ".", "."], 
    [".", ".", "."], 
    [".", ".", "."]
]


# set the score of the game
# score = [0, 0]


# a function to print the grid
""" displays the current state of the board (grid) """
def displayGrid(grid=grid):
    vertical_line = "|"
    horizontal_line = "-----"
    space = " "

    board = ""
    # board += (horizontal_line * 7 ) + "-\n"
    board += vertical_line + "[" + str(grid[0][0]) + space + horizontal_line \
        + space + str(grid[0][1]) + space + horizontal_line \
            + space + str(grid[0][2]) +  "]" + vertical_line + "\n"
    board += vertical_line + "[" + str(grid[1][0]) + space + \
        horizontal_line + space + str(grid[1][1]) + space + \
            horizontal_line + space + str(grid[1][2]) +  "]" + vertical_line + "\n"
    board += vertical_line + "[" + str(grid[2][0]) + space + \
        horizontal_line + space + str(grid[2][1]) + space + \
            horizontal_line + space + str(grid[2][2]) +  "]" + vertical_line + "\n"
    # board += (horizontal_line * 7) + "-\n"

    printf(board)


# after we set token we call displayGrid so that it won't be called explicitly
""" moves a token to a position when the game starts, using the x_index and y_index. """
def setToken(x_index, y_index, token='#', grid=grid):
    if checkBounds(x_index, y_index):
        if isPositionEmpty(x_index, y_index):
            grid[x_index][y_index] = token
            printf("token set at position ({}, {})".format(x_index, y_index))
        else:
            printf("position ({}, {}) is filled".format(x_index, y_index))
    else:
        printf("position ({}, {}) is out of bounds".format(x_index, y_index))
    
    # call displayGrid after the output of setToken
    displayGrid()


# check if position is empty before you set a token there
""" A position must be empty before you can set a token there """
def isPositionEmpty(x_index, y_index, grid=grid):
    if grid[x_index][y_index] == ".":
        return True
    else:
        return False


# check bounds - check the min-max of position index
""" A position must line within the grid """
def checkBounds(x_index, y_index, grid=grid):
    grid_size = len(grid) - 1
    if (x_index >= 0 and x_index <= grid_size) and (y_index >= 0 and y_index <= grid_size):
        return True
    else:
        return False


# move token
""" move token to a new position """
def moveToken(x_index, y_index, nx_index, ny_index, token='#', grid=grid):
    if checkBounds(x_index, y_index) and checkBounds(nx_index, ny_index):
        if isPositionEmpty(x_index, y_index):
            printf("can not move from position ({}, {}), there is no token there".format(x_index, y_index))

            # make a suggestion
            makeSuggestion(x_index, y_index)

        else:
            if isPositionEmpty(nx_index, ny_index):
                grid[x_index][y_index] = "."
                grid[nx_index][ny_index] = token

                printf("moved from position ({}, {}) to ({}, {})".format(x_index, y_index, nx_index, ny_index))

                # display grid
                displayGrid()

                # check if there is a win after a move and restart
                if checkWin():
                    printf("There is a win")

                    restart()
            else:
                printf("can not move to position ({}, {}), there is a token there".format(nx_index, ny_index))
            
    else:
        printf("position ({}, {}) or ({}, {}) is out of bounds".format(x_index, y_index, nx_index, ny_index))


# restart the game
""" call restart to clear the board """
def restart(grid=grid):
    grid_size = len(grid)

    for x in range(grid_size):
        for y in range(grid_size):
            grid[x][y] = "."
    
    # display grid after restart
    displayGrid()


# make suggestion on move when position is out of bounds or is empty
# above we called makeSuggestion in isPositionEmpty because makeSuggestion would kind of depend on checkBounds
""" suggest a move when position is out of bounds """
def makeSuggestion(x_index, y_index, grid=grid):
    grid_size = len(grid)

    printf("some moves you could make")

    for x in range(grid_size):
        for y in range(grid_size):
            if x_index == x and y_index == y:
                continue
            else:
                printf("({}, {})".format(x, y), end="")
    
    printf('')
                
    
# check whether there is a win
# at diagonals, the indices are the same
# check if isPositionEmpty and has token
""" when tokens are on row0, row1, row2, col0, col1, col2, diag00 or diag02 then there is a win """
def checkWin(grid=grid):
    # row0
    if not isPositionEmpty(0, 0) and not isPositionEmpty(0, 1) and not isPositionEmpty(0, 2):
        return True
    # row1
    elif not isPositionEmpty(1, 0) and not isPositionEmpty(1, 1) and not isPositionEmpty(1, 2):
        return True
    # row2
    elif not isPositionEmpty(2, 0) and not isPositionEmpty(2, 1) and not isPositionEmpty(2, 2):
        return True
    # col0
    elif not isPositionEmpty(0, 0) and not isPositionEmpty(1, 0) and not isPositionEmpty(2, 0):
        return True
    # col1
    elif not isPositionEmpty(0, 1) and not isPositionEmpty(1, 1) and not isPositionEmpty(2, 1):
        return True
    # col2
    elif not isPositionEmpty(0, 2) and not isPositionEmpty(1, 2) and not isPositionEmpty(2, 2):
        return True
    # diag00
    elif not isPositionEmpty(0, 0) and not isPositionEmpty(1, 1) and not isPositionEmpty(2, 2):
        return True
    # diag02
    elif not isPositionEmpty(0, 2) and not isPositionEmpty(1, 1) and not isPositionEmpty(2, 0):
        return True
    else:
        return False


# quit/exit
""" kill the program """
def quit():
    exit(0);


# write the output into a file
def printf(text, file_name = "output.txt"):
    with open(file_name, "a+") as f:
        print(text, file=f)



# start the program
""" call start to start the program """
def start():
    printf("#" * 50)
    displayGrid()
    setToken(1, 0)
    moveToken(1, 0, 1, 1)
    setToken(1, 0)
    setToken(2, 0)
    moveToken(1,1, 0, 1)
    moveToken(0, 1, 0, 2)
    moveToken(1, 0, 1, 1)


start()
