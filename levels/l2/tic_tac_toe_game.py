#This code was adapted from https://www.scaler.com/topics/tic-tac-toe-python/

###################################################################################
# Add code here to print a welcome and some basic instructions for the game.
# The grid shows what number corresponds to what position on the
# tic tac toe board (this is what is entered when the player is choosing their
# position). We included it for you to save you the hassle of formatting, however
# feel free to modify it if you wish (～￣▽￣)～

print("\n")
print("\t      |      |")
print("\t    1 |  2   |  3")
print('\t______|______|______')
print("\t      |      |")
print("\t   4  |  5   |  6")
print('\t______|______|______')
print("\t      |      |")
print("\t   7  |  8   |  9")
print("\t      |      |")
print("\n")
##################################################################################

# This method handles drawing the grid on the screen,
# it takes a list as an argument
def tictactoe_grid(value):
    # print the first three boxes of the 3X3 game board
    print("\n")
    print("\t      |      |")
    print("\t    {} |  {}   |  {}".format(value[0], value[1], value[2]))
    print('\t______|______|______')
    # print the second three boxes of the 3X3 game board
    print("\t      |      |")
    print("\t   {}  |  {}   |  {}".format(value[3], value[4], value[5]))
    print('\t______|______|______')
    print("\t      |      |")
    # print the last three boxes of the 3X3 game board
    print("\t  {}   |  {}   |  {}".format(value[6], value[7], value[8]))
    print("\t      |      |")
    print("\n")



# This method creates and displays the scoreboard,
# it takes a dictionary as an argument
def my_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t         SCOREBOARD             ")
    print("\t--------------------------------")

    list_of_the_two_players = list(score_board.keys())
    print("\t   ", list_of_the_two_players[0], "\t    ",
          score_board[list_of_the_two_players[0]])
    
    print("\t   ", list_of_the_two_players[1], "\t    ",
          score_board[list_of_the_two_players[1]])

    print("\t--------------------------------\n")


# This method checks the board for any winning combinations
# and returns true if yes, and false if none. It takes 2
# dictionaries as arguments
def win_validate(position_player, player_current):

    # Below are all the possible winning combinations for the game
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8],
                        [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Check for any winning combinations
    for i in win_combinations:
        if all(j in position_player[player_current] for j in i):

            # If there is a winning combination, return true
            return True

    # If there is no winning combination, return false
    return False


# This method determines if the players have reached a tie,
# it takes a dictionary as an argument and returns true if they have
# and false if they have not (meaning someone has won)
def tie_validate(position_player):
    if len(position_player['X']) + len(position_player['O']) == 9:
        return True
    return False

# This method creates the game and makes it playable
def game_single(player_current):
    value = [' ' for i in range(9)]

    position_player = {'X': [], 'O': []}

    while True:
        #draw the board
        tictactoe_grid(value)

        try:
            #tell the players whos turn it is
            print(player_current,
                  "'s turn: ",
                  end="")
            chance = int(input())
        except ValueError:
            ######################################################################
            # This is what is triggered when a character other than an integer is 
            # entered when selecting a position to play
            #####################################################################
            continue

        
        #to check if the position requested is already filled or not
        if value[chance - 1] != ' ':
            print("Oops! The position is already filled. Please try again!")
            continue

        # update the gameboard's status
        value[chance - 1] = player_current
        # update the players positions on the grid
        position_player[player_current].append(chance)

        # check for a win
        if win_validate(position_player, player_current):
            tictactoe_grid(value)
            print("Hurray! You nailed it! ", player_current,
                  " has won the game!")
            print("\n")
            return player_current

        # check for a tie
        if tie_validate(position_player):
            tictactoe_grid(value)
            print("It was close! Game ended in a draw")
            print("\n")
            return 'D' # D for 'draw'

        # this changes who's turn it is
        if player_current == 'X':
            player_current = 'O'
        else:
            player_current = 'X'


# This is the main 'method', it is the first thing 
# that runs when tic_tac_toe_game.py starts
if __name__ == "__main__":

    #get the players' names
    print("The First player's name")
    print("\n")

    print("The Second player's name")
    print("\n")

    #################################################################################################
    # Add code here for checking the player names are not the same.
    # If they are the same, you should display a message saying it is not
    # allowed, and ask them to input another name (this should be contained in a loop
    # structure so that this basic action does not break your entire program!)
    
    ###################################################################################################

    # The first player is the one who goes first
    player_current = player_first

    # For storing the player's character choice
    player_choice = {'X': "", 'O': ""}

    # Storing the two possible options available for the tic tac toe Python game
    option = ['X', 'O']

    # Storing the information for the scoreboard
    score_board = {player_first: 0, player_second: 0}

    # Calling the method that displays the scoreboard
    my_scoreboard(score_board)


    # This loop means the game can be played any number of times until
    # a player chooses to exit
    while True:
        # Menu displayed to the players when the game first starts
        print(
            ", you get to choose what character you want to play the game with:"
        )
        print("Please press 1 for X")
        print("Please press 2 for O")
        print("Please press 3 for Exit")

        # this is used to check the input (to ensure its valid)
        while True:
            try:
                # get the choice from the player and check it is a whole number before continuing
                the_choice = int(input())
                if the_choice == 1 or the_choice == 2 or the_choice == 3:
                    break
                # this occurs if it is not a number (well not an integer)
                print("Invalid input, please try again: ")
            except ValueError:
                print("Invalid input, please try again: ")
                continue
            
        
        # the logic for the character chosen by the first player
        if the_choice == 1:
            player_choice['X'] = player_current
            if player_current == player_first:
                player_choice['O'] = player_second
            else:
                player_choice['O'] = player_first

        elif the_choice == 2:
            player_choice['O'] = player_current
            if player_current == player_first:
                player_choice['X'] = player_second
            else:
                player_choice['X'] = player_first

        elif the_choice == 3:
            # to quit the game
            print("Exiting...")

        else:
            print("Invalid option entered, please try again\n")

        # check if the recent move has resulted in a winning combination 
        winner = game_single(option[the_choice - 1])

        # declare the winner (check if it is a tie first)
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
            #update the scoreboard
            my_scoreboard(score_board)

        #######################################################################
        # Add code here for swapping who gets to play first after each game.
        # Hint: the current player's turn is stored in player_current so you
        # should update that variable with the one you want to swap it to.
        # You will also need to update the print statement we modified in the 
        # PDF otherwise it will only display the first player's name.

        #######################################################################
        