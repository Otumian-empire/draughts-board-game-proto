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
score = [0, 0]


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

    print(board)


""" moves a token to a position when the game starts, using the x_index and y_index. """
def setToken(x_index, y_index, token='#', grid=grid):
    if checkBounds(x_index, y_index):
        if isPositionEmpty(x_index, y_index):
            grid[x_index][y_index] = token
        else:
            print("position ({}, {}) is filled".format(x_index, y_index))
    else:
        print("position ({}, {}) is out of bounds".format(x_index, y_index))


# check if position is empty before you set a token there
""" A position must be empty before you can set a token there """
def isPositionEmpty(x_index, y_index, grid=grid):
    if grid[x_index][y_index] == ".":
        return True

    makeSuggestion(x_index, y_index)
    return False


# check bounds - check the min-max of position index
""" A position must line within the grid """
def checkBounds(x_index, y_index, grid=grid):
    grid_size = len(grid) - 1
    if (x_index >= 0 and x_index <= grid_size) and (y_index >= 0 and y_index <= grid_size):
        return True
    
    return False


# move token
""" move token to a new position """
def moveToken(x_index, y_index, nx_index, ny_index, token='#', grid=grid):
    if checkBounds(x_index, y_index) and checkBounds(nx_index, ny_index):
        if not isPositionEmpty(x_index, y_index) and isPositionEmpty(nx_index, ny_index):
            grid[x_index][y_index] = "."
            grid[nx_index][ny_index] = token
        else:
            print("can not move from position ({}, {}) to ({}, {}), \
                there may be a piece at latter or none at former".format(x_index, y_index,nx_index, ny_index))
    else:
        print("position ({}, {}) or ({}, {}) is out of bounds".format(x_index, y_index, nx_index, ny_index))


# restart the game
""" call restart to clear the board """
def restart(grid=grid):
    grid_size = len(grid)

    for x in range(grid_size):
        for y in range(grid_size):
            grid[x][y] = "."
    
    displayGrid()


# make suggestion on move when position is out of bounds or is empty
# above we called makeSuggestion in isPositionEmpty because makeSuggestion would kind of depend on checkBounds
""" suggest a move when position is out of bounds """
def makeSuggestion(x_index, y_index, grid=grid):
    grid_size = len(grid)

    print("some moves you could make")
    for x in range(grid_size):
        for y in range(grid_size):
            if x_index == x and y_index == y:
                continue
            else:
                print("position ({}, {})".format(x, y))
                
    
# check whether there is a win
""" when tokens are on row0, row1, row2, col0, col1, col2, diag00 or diag02 then there is a win """
def checkWin():
    pass

    
# start the program
""" call start to start the program """
def start():
    # print(grid)

    # displayGrid(grid)

    # setToken(0,1, '#')
    # displayGrid()
    # setToken(0,2, '#')
    # displayGrid()

    # setToken(0,1, '#')
    # displayGrid()
    # setToken(0,1, '#')
    # displayGrid()

    displayGrid()
    # setToken(0,1)
    # displayGrid()
    # setToken(0,1)
    # displayGrid()
    # setToken(0,3)
    # displayGrid()
    setToken(0,0)
    displayGrid()
    moveToken(0, 0, 0, 1)
    displayGrid()
    moveToken(0, 1, 2, 1)
    displayGrid()
    restart()


start()
