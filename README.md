# draughts-board-game-proto (DBGP)
I didn't find a cool name, maybe, i'd change it to rice-head. I do basic things like this on my leisure time mostly week ends or when there is no work or i want to escape from stress.
<br>
This is a replication of the draught (same as checkers) game with only three pieces (i call it tokens) for each player. The board has nine vertices.
This version involves moving the token and running the program anytime you make changes to the instructions.
Itb was meant for two-players.

# to play
The participant(s) must set the tokens on the board at a particular vertex, alternatively between the participant(s) until all six tokens, for a single player, three tokens, has been position at different vertices on the board.

# to move a token
The current vertex (position) must have a token and the destination vertex must be empty. There is a possibility that a token would be moved two clicks (vertices/positions) at a go. This wasn't meant to happen, if it happens or happened.

# to set a token
The vertex must be empty

# to win 
All three tokens must line up horizontally on the first, second or third row.
<br>
All three tokens must line up vertically on the first, second or third column.
<br>
All three tokens must line up diagonally from top-left, center-center and bottom-right or diagonally from top-right, center-center and bottom-left

# functions used
## displayGrid
This displays the grid (board). Some of the functions like moveToken and setToken calls displayGrid. This function takes an argument, grid which is default, set to the global grid.<br>
`Usage 1: displayGrid(grid=grid)`<br>
`Usage 2: displayGrid()`

## moveToken
moveToken(x_index, y_index, nx_index, ny_index, token='#', grid=grid)
This moves a token to a new position. It takes six arguments, of which the first two are the x-index and y-index of the current position, the next two are the x-index and y-index of the new position. The last two are the token which is by default set to '`#`' and grid which is the global grid which also default.
`Usage 1: moveToken(x_index, y_index, nx_index, ny_index, token='#', grid=grid)`<br>
`Usage 2: moveToken(x_index, y_index, nx_index, ny_index)`

## checkWin
This function returns a boolean, True if a play has won and calls restart. This also take the global grid as a default argument.<br>
`Usage 1: checkWin(grid=grid)`<br>
`Usage 2: checkWin()`<br>
Read [more](#to-win) on how to win

## setToken
This sets a token an an empty vertex on the grid. It take four arguments, the first two are the x-index and the y-index of the position, and the rest are `token = "#"` and `grid=grid`<br>
`Usage: setToken(x_index, y_index)`

## isPositionEmpty
This function checks is a vertex is empty, i.e the value there is ' `.` ' and then returns a boolean, True else False. It takes three arguments, the first two are the x-index and the y-index of the vertex and the last is `grid=grid`<br>
`Usage: isPositionEmpty(x_index, y_index)`

## restart
This function assigns ' `.` ' to all the vertices of the grid and calls displayGrid. This means, it clears the board. This takes one argument which is `grid=grid`<br>
`Usage: restart()`

## start
This function runs the program after you have called all the functions you need. start is like 'the' main function.<br>
`Usage: start()`

## makeSuggestion
This prints out a suggestion of vertices that a play may opt for. This is called in moveToken when the play tries to move a token from an empty vertex. This function takes three arguments, the first two are the x-index and y-index of position and the last is `grid=grid`. The vertices returned excludes the x-index and y-index of position.<br>
`Usage: makeSuggestion(x_index, y_index)`

## checkBounds
This function checks if a given index is greater than the size of the grid (i.e three in this case) or the give index is less than zero (An index may start from zero). This returns a boolean. setToken and moveToken calls checkBounds.<br>
This function takes three arguments, the first two are the x-index and y-index of position and the last is `grid=grid`.

## printf
This function outputs the result after call start into a file. This is a modified print function to direct output to a file instead of the stdout. It take two arguments, text, which a string output and then a file name which is by default `file_name='output.txt'`<br>
`Usage 1: printf(text)`<br>
`Usage 2: printf(text, file_name)`

## quit
This kills the program. It takes no argument. It calls exit(0)<br>
`Usage: quit()`

# meaning of tokens
'`#`' - pound sign represents an occupied vertex and '`.`' - dot represents an empty vertex.

# some to-do's
* change all positions into a tuple
* edit the read me
* find a salient name or keep the master-mind-super-ultra something name
* implement the score (maybe, sqlite3)
* look into a web version (maybe)

# vision
Been able to issue commands and arguments and seeing the output (grid) will be awesome and i'm looking forward to it. 

