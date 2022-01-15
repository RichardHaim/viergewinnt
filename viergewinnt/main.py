import startup_screen
import end_screen


def playfield_init():
    """
    add docstring

    column references >>
        1 == 1 >> diff 0
        2 == 3 >> diff 1
        3 == 5 >> diff 2
        4 == 7 >> diff 3
        5 == 9 >> diff 4
        6 == 11 >> diff 5

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


    playfield = [
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        ["| ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " |"],
        [" _", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_ "],
        ["  ", "1", " ", "2", " ", "3", " ", "4", " ", "5", " ", "6", "  "]
    ]
    return playfield





def playfield_print(p: list):
    """
    add docstring

    Returns
    -------

    """
    for row in p:
        listToStr = ' '.join(map(str,row))
        print(listToStr)
    print("")



def the_game(player):
    """
    add docstring

    Returns
    -------

    """

    print(player)
    if player == "2":
        player1 = input(f'Player 1 please enter your name: ')
        player2 = input(f'Player 2 please enter your name: ')
        print(player1, player2)
    else:
        player_solo = input(f'Please enter your name: ')
        player_ai = "Computer"
        print(player_solo, player_ai)

    field = playfield_init()
    playfield_print(field)

    winner = True  #code keeps running until someone won, or draw
    while not winner:
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
    player = input(f'Enter 1 to play against your computer, enter 2 to play against human opponent. Enter x to exit ')
    player_check = False
    if player == "1" or player == "2":
        player_check = True
        the_game(player)  # Game starts here
    elif player == "x":
        return print(f'EXIT')
    while player_check == False:
        player = input(
            f'{player} is incorrect, please enter 1 to play against your computer, enter 2 to play against human opponent. Enter x to exit ')
        if player == "1" or player == "2":
            player_check = True
            the_game(player)  # Game starts here
        elif player == "x":
            return print(f'Programm beendet')
    # print(player)  used for checks





if __name__ == '__main__':
    startup()