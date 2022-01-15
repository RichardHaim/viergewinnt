'''
CHANGES:
moved play_field from playfield_init to the_game + removed playfield_init --> will be updated in the_game
added rules
added input for player moves
'''

import startup_screen
import end_screen
import rules


def playfield_print(play_data: list):
    """
    add docstring

    column references in playfield >>
        1 == 1 >> diff 0
        2 == 3 >> diff 1
        3 == 5 >> diff 2
        4 == 7 >> diff 3
        5 == 9 >> diff 4
        6 == 11 >> diff 5

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




def player_move():
    field:int = 0
    try:
        field = int(input(f'Please enter the column you want to place your move (1 - 6): '))
        if field >= 1 and field <= 6:
            return field
        else:
            print(f'Your input is not valid, please enter a number from 1 to 6')
            player_move()
    except:
        print(f'Your input is not valid')
        player_move()



def the_game(player):
    """
    add docstring

    Returns
    -------

    """

    play_data = [
        [0, 0, 0, 0, 0, 0],   # row 7
        [0, 0, 0, 0, 0, 0],   # row 6
        [0, 0, 0, 0, 0, 0],   # row 5
        [0, 0, 0, 0, 0, 0],   # row 4
        [0, 0, 0, 0, 0, 0],   # row 3
        [0, 0, 0, 0, 0, 0],   # row 2
        [0, 0, 0, 0, 0, 0]    # bottom row
    ]
    # 0 = empty
    # 1 = player1
    # 2 = player2 / AI

    if player == "2":
        player1 = input(f'Player 1 please enter your name: ')
        player2 = input(f'Player 2 please enter your name: ')
        print("")
    else:
        player_solo = input(f'Please enter your name: ')
        player_ai = "Computer"
        print("")

    playfield_print(play_data)

    winner = False  #code keeps running until someone won, or draw
    while not winner:
        #todo player vs player

        #todo player vs ki
        field = player_move()
        print(field)
        # todo store move + next player

        # case1 = out of range bzw Eingabe Blödsinn
        # if move >= 1 and move <= 7:
        # case2 = Spalte voll
        # case3 = frei
        exit()

        #todo player change after move

        pass
        #TODO create variable that stores information of winning player
        #TODO create variable to store infomation on ending screen
        #TODO open correct ending screen based on winner
        end_screen.winner(player) #TODO change player to winning player, not to imported player
        end_screen.loser()
        end_screen.draw()


def startup():
    """
    add docstring

    Returns
    -------

    """
    startup_screen.titlescreen()
    rules.rules_set()

    player = input(f'Enter 1 to play against your computer, enter 2 to play against human opponent. Enter x to exit: ')
    player_check = False
    if player == "1" or player == "2":
        player_check = True
        the_game(player)  # Game starts here
    elif player == "x":
        return print(f'EXIT')
    while player_check == False:
        player = input(
            f'{player} is incorrect, please enter 1 to play against your computer,'
            f'enter 2 to play against human opponent. Enter x to exit: ')
        if player == "1" or player == "2":
            player_check = True
            the_game(player)  # Game starts here
        elif player == "x":
            return print(f'EXIT')
    # print(player)  used for checks





if __name__ == '__main__':
    startup()