# Tic Tac Toe - Beginner
# King of Code
# June 2021

# DISPLAY FUNCTION
def displayBoard(board):
    #way 1
    print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))
    print("-----")
    print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
    print("-----")
    print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))

    """
    #way 2
    for i in range(0,3):
        print(str(board[i*3]) + "|" + str(board[i*3+1]) + "|" + str(board[i*3+2]))
        if i < 2:
            print("-----")
    """

# CHECK RESULT FUNCTION
def checkGameResult(board, shape):
    # horizontally - 0,1,2 3,4,5 6,7,8
    # vertically - 0,3,6 1,4,7, 2,5,8
    # diagnolly - 0,4,8 2,4,6
    winScenario = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    #check win
    for scenario in winScenario:
        win=True
        for i in scenario:
            if board[i]!=shape:
                win=False
        if win:
            return shape

    #check tie
    tie=True
    for i in board:
        if type(i) == type(1):
            tie=False
    if tie:
        return "T"

    #no winner or tie
    return None


userInput='y'
#program loop
#while the user input is not n
while userInput != 'n':
    board = [0,1,2,
             3,4,5,
             6,7,8]
    gameResult = None
    player = 1

    #game loop - alternate players
    #while no winner and no tie
    while gameResult == None:
        #decide shape to be used
        shape='X'
        if player == -1:
            shape='O'

        #display the board
        displayBoard(board)

        #prompt the user to select a cell
        userSelection=10
        while not int(userSelection) in board:
            userSelection=input("Please type the number of the cell you would like to choose: ")

        #place the player's shape in to the cell
        board[int(userSelection)] = shape

        #check to see if there is a winner or tie
        gameResult = checkGameResult(board, shape)

        #switch players
        player *= -1

    #display final board
    displayBoard(board)

    #announce the results (winner or tie)
    if gameResult == "T":
        print("The game ended in a TIE!")
    else:
        print(gameResult + " won the game!")

    #prompt user to play again or quit
    userInput = None
    while userInput != "n" and userInput != "y":
        userInput = input("Would you like to play again (y or n)? ")