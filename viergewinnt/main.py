import startup_screen


class Playfield():
    """
    add docstring
    """


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


    def playfield_update():
        """
        add docstring

        Returns
        -------

        """
        pass


class Game():
    """
    where the magic happens
    add docstring
    """
    def init():
        field = Playfield.playfield_init()
        Playfield.playfield_print(field)




class Startup():
    """
    add docstring
    """
    startup_screen.titlescreen()
    def player_check():
        """
        add docstring

        Returns
        -------

        """
        player = input(f'Enter ki to play against your computer, enter p to play against human opponent. Enter x to exit ')
        player_check = False
        if player == "ki" or player == "p":
            player_check = True
            Game.init()     # Game starts here
        elif player == "x":
            return print(f'Programm beendet')
        while player_check == False:
            player = input(f'{player} is incorrect, please enter ki to play against your computer, enter p to play against human opponent. Enter x to exit ')
            if player == "ki" or player == "p":
                player_check = True
                Game.init()     # Game starts here
            elif player == "x":
                return print(f'Programm beendet')
        #print(player)  used for checks

    player_check()




if __name__ == '__main__':
    """
    add docstring
    """
    Startup()


