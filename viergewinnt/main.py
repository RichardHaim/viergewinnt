'''
CHANGES:
add play_data_update
'''

import startup_screen, end_screen, rules


def playfield_print(play_data):
    """prints the played moves onto the playfield

    The play_data is stored in a format that is convenient to use for programming,
    but does not look good when printing. This method adds all moves to the playfield,
    so the moves can be printed in an easy to read format.

    Returns
    -------

    """
    playfield = [
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        [" -", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "- "],
        ["  ", "1", " ", "2", " ", "3", " ", "4", " ", "5", " ", "6", "  "]
    ]

    playfield_pos = 1
    playfield_row = 0

    for row in play_data:
        for pos in row:
            if pos == 1:
                playfield[playfield_row][playfield_pos] = "X"
            if pos == 2:
                playfield[playfield_row][playfield_pos] = "O"
            playfield_pos += 2
        playfield_row += 1
        playfield_pos = 1

    for row in playfield:
        listToStr = ' '.join(map(str,row))
        print(listToStr)

    print("")




def player_move(actual_player):
    #field = 0
    try:
        field = int(input(f'{actual_player}, please enter the column you want to place your move (1 - 6): '))
        if field >= 1 and field <= 6:
            return field
        else:
            print(f'Your input is not valid, please enter a number from 1 to 6')
            player_move(actual_player)
    except:
        print(f'Your input is not valid')
        player_move(actual_player)




def play_data_update(field, play_data, actual_player, player_fig):
    """Checks if selected column is free to select + places move

    Returns
    -------
    play_data
    player_move
    """

    # TODO 1) check, if selected column is free to select (max-row)
    line = 6
    while line >= 0:
        if play_data[line][field-1] == 0:
            play_data[line][field-1] = player_fig
            print("")
            playfield_print(play_data)
            return play_data

            #TODO Gewinnabfrage

        line -= 1
    print(f'Column {field} is full and cannot be selected')
    field = player_move(actual_player)
    play_data_update(field, play_data, actual_player, player_fig)




def the_game(player):
    """add docstring

    Returns
    -------

    """

    play_data = [
        [0, 0, 1, 0, 0, 0],   # row 7
        [0, 0, 1, 0, 0, 0],   # row 6
        [0, 0, 1, 0, 0, 0],   # row 5
        [0, 0, 1, 0, 0, 0],   # row 4
        [0, 0, 1, 0, 0, 0],   # row 3
        [0, 0, 2, 0, 0, 0],   # row 2
        [0, 0, 1, 0, 0, 0]    # bottom row
    ]
    # 0 = empty
    # 1 = player1
    # 2 = player2 / AI

    if player == "2":
        player1_name = input(f'Player 1 please enter your name: ')
        player2_name = input(f'Player 2 please enter your name: ')
        print("")
    else:
        player1_name = input(f'Please enter your name: ')
        player2_name = "Computer"

        #TODO AI difficulty -> speichern in variable + Übergabe an AI-Methode

        print("")

    playfield_print(play_data)

    winner:bool = False  #code keeps running until someone won, or draw
    while not winner:
        actual_player_name = player1_name
        player_fig = 1
        field = player_move(actual_player_name)
        play_data = play_data_update(field, play_data, actual_player_name, player_fig)
        #TODO player change
        #TODO CREATE PLAY LOOP

        exit()

        #TODO create variable that stores information of winning player
        #TODO create variable to store infomation on ending screen
        #TODO open correct ending screen based on winner

        end_screen.winner(player) #TODO change player to winning player, not to imported player
        end_screen.loser()
        end_screen.draw()


def startup():
    """Starts the game by asking if player wants to play vs AI, human opponent, or quit

    Returns
    -------
    exit in case of "x"

    """
    startup_screen.titlescreen()
    rules.rules_set()

    player = input(f'Enter 1 to play against your computer, enter 2 to play against human opponent. Enter x to exit: ')
    player_check = False
    if player == "1" or player == "2":
        player_check = True
        the_game(player)  # actual game starts here
    elif player == "x":
        return print(f'EXIT')
    while player_check == False:
        player = input(
            f'{player} is incorrect, please enter 1 to play against your computer,'
            f'enter 2 to play against human opponent. Enter x to exit: ')
        if player == "1" or player == "2":
            player_check = True
            the_game(player)  # actual game starts here
        elif player == "x":
            return print(f'EXIT')






if __name__ == '__main__':
    startup()