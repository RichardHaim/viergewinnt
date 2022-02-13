import random
from os import system, name



class Playfield():
    ''' initializes the playfield
        prints the playfield
        updates the played moves
        reviews if the game is won/draw
        cleans the screen after after each move
    '''

    def playdata_init(self):
        ''' initializes the playfield data
        The playfield data is stored in a list containing 0 (empty), 1 (player 1), 2 (player 2), 3 (AI)

        Returns
        -------
        play_data: the updated playfield data
        '''
        play_data = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 0, 0, 0]  # bottom row
        ]
        return play_data


    def winner_check(self, p_data, p_name, p_ID):
        ''' passes over to winner_validation every move and calls winselector if p_ID != 69

        Parameters
        ----------
        p_data: the playfield data
        p_name: name of current playner
        p_ID: ID of current player: 1 (player 1), 2 (player 2), 3 (AI)

        Returns
        -------
        nothing

        '''

        eg = Endgame()

        # check 4 in row
        p_ID = self.winner_validation(p_ID, p_data)
        if p_ID != 69:
            eg.winselector(p_ID, p_name)


    def winner_validation(self, p_ID, p_data):
        '''checks if game is won/draw and calls winselector if true

        Parameters
        ----------
        p_ID: ID of current player: 1 (player 1), 2 (player 2), 3 (AI)
        p_data: the playfield data

        Returns
        -------
        69: if no winner/draw
        p_ID: if winner/draw
        '''

        #check 4 in row
        row = 0
        while row <= 6:
            col = 0
            while col <= 2:
                if (p_data[row][col] == p_ID and p_data[row][col + 1] == p_ID and
                        p_data[row][col + 2] == p_ID and p_data[row][col + 3] == p_ID):
                    return p_ID
                col += 1
            row += 1

        # check 4 in column
        col = 0
        while col <= 5:
            row = 0
            while row <= 3:
                if (p_data[row][col] == p_ID and p_data[row + 1][col] == p_ID and
                p_data[row + 2][col] == p_ID and p_data[row + 3][col] == p_ID):
                    return p_ID
                row += 1
            col += 1

        # check 4 diagonal
        # starts at 0/0 and checks diagonal left top to right bottom until column index 2
        # resumes at 3/0 and checks diagonal right top to left bottom until column index 5
        # jumps into next row if no winner found
        row = 0
        while row <= 3:
            col = 0
            while col <= 5:
                while col <= 2:
                    if (p_data[row][col] == p_ID and p_data[row + 1][col + 1] == p_ID
                     and p_data[row + 2][col + 2] == p_ID and p_data[row + 3][col + 3] == p_ID):
                        return p_ID
                    col += 1
                if (p_data[row][col] == p_ID and p_data[row + 1][col - 1] == p_ID
                        and p_data[row + 2][col - 2] == p_ID and p_data[row + 3][col - 3] == p_ID):
                    return p_ID
                col += 1
            row += 1

        # check draw
        col = 0
        non_zero_counter = 0
        while col <= 5:
            if p_data[0][col] != 0:
                non_zero_counter += 1
            col += 1
        if non_zero_counter == 6:
            p_ID = 99
            return p_ID

        # no winner/draw
        return 69 #random number used to prevent winner_check to go into Endgame


    def play_data_update(self, selected_field, p_data, p_name, p_ID):
        """Checks if selected column is free to select + places move

        Returns
        -------
        p_data: playfield data updated with player token
        """

        notfinished = True
        while notfinished:
            line = 6
            while line >= 0:
                validation = self.play_data_validation(line, selected_field, p_data)
                if validation:
                    p_data[line][selected_field-1] = p_ID
                    return p_data
                line -= 1
            if p_ID != 3:
                print(f'Column {selected_field} is full and cannot be selected')
                selected_field = Players().player_move(p_name)
            else:
                selected_field = random.randint(0, 5)


    def play_data_validation(self, line, selected_field, p_data):
        ''' validates if the selected column is full

        Parameters
        ----------
        line: actual line
        selected_field: field that is selected
        p_data: playfield with play data

        Returns
        -------
        True: column is not full, field can be selected
        False: column is full, field cannot be selected
        '''
        if p_data[line][selected_field-1] == 0:
            return True
        return False


    def print_playfield(self, p_data):
        '''Prints the playfield
        This method is purely for optical reasons to print the playfield in an easy to read way

        Parameters
        ----------
        p_data: playfield data

        Returns
        -------
        printout of the playfield

        '''
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

        for row in p_data:
            for pos in row:
                if pos == 1:
                    playfield[playfield_row][playfield_pos] = "X"
                if pos == 2 or pos == 3:
                    playfield[playfield_row][playfield_pos] = "O"
                playfield_pos += 2
            playfield_row += 1
            playfield_pos = 1

        print("")
        for row in playfield:
            listToStr = ' '.join(map(str, row))
            print(listToStr)


    def cleansreen(self):
        '''clears the playing field after every move

        Returns
        -------
        noting
        '''
        if name == "nt":
            _ = system('cls')
        else:
            _ = system('clear')



class Players():
    ''' stores player names
        allocates player ID to player name
        verifies player moves
    '''
    def startup(self, p_ID):
        '''Asks for player names (input)

        Parameters
        ----------
        p_ID: number of player (1 or 2)

        Returns
        -------
        p_name: name of the player that was added via input
        '''
        p_name = input(f'Player {p_ID} please enter your name: ')
        return p_name



    def player_change(self, p_ID, p1, p2):
        '''changes the actual player

        Parameters
        ----------
        p_ID: number of actual player; 1 = player1, 2 = player2

        Returns
        -------
        p1 or p2, depending on who the actual player was
        '''
        if p_ID == 1:
            return p2
        else:
            return p1



    def player_move(self, p_name):
        '''gets input of desired move and validates, if input is correct

        Parameters
        ----------
        p_name: name of actual player

        Returns
        -------
        field: the column in which the player wants to place the token
        '''
        notfinished = True
        while notfinished:
            selected_field = input(f'\n{p_name}, enter the column you want to place your token or enter q/Q to quit >> ')
            if selected_field == "Q" or selected_field == "q":
                print("\nTHANK YOU FOR PLAYING")
                exit()
            validation = self.player_move_validation(selected_field)
            if validation:
                return int(selected_field)
            else:
                print(f'No valid input')
            # try:
            #     selected_field = int(selected_field)
            #     if selected_field >= 1 and selected_field <= 6:
            #         return selected_field
            #     else:
            #         print(f'No valid input')
            # except:
            #     print(f'No valid input')



    def player_move_validation(self, selected_field):
        '''validates if player input is correct

        Parameters
        ----------
        selected_field: player input

        Returns
        -------
        True: input is correct
        False: input is incorrect
        '''
        try:
            selected_field = int(selected_field)
            if selected_field >= 1 and selected_field <= 6:
                return True
            else:
                return False
        except:
            return False




class Game():
    ''' runs the game
    '''
    pf = Playfield()
    pf.cleansreen()


    def titlescreen(self):
        """prints titlescreen

        Returns
        -------
        nothing
        """
        print ('''
***********************************
XOXO        4 gewinnt          XOXO
***********************************
    ''')


    def rules_set(self):
        '''print rules of the game

        Returns
        -------
        nothing
        '''

        print ('''
RULES OF THE GAME:
The game is played on a vertical board which has seven columns and six rows. 
The aim for both players is to make a straight line of four OWN pieces (in our version of the game the pieces will be
"X" and "O"). The Line can be vertical, horizontal or diagonal. Moves are made alternatively, one by turn.
If none reaches to put 4 pieces in a line, its a draw. 
        ''')


    def ai_vs_human(self):
        '''asks if player wants to play pvp or pvc

        Returns
        -------
        dec: as parameter for the gameloop; holds information if opponent is AI or human
        '''
        dec = input(f'To play against an human opponent press 1, to play against the computer press 2. To exit press q/Q >> ')
        if dec == "q" or dec == "Q":
            print("\nGood Bye!")
            exit()
        elif dec == "1" or dec == "2":
            self.gameloop(dec)
        else:
            self.ai_vs_human()


    def gameloop(self, fiend):
        ''' the actual game

        Parameters
        ----------
        fiend: contains information, if pvp (1) or pvc (2)

        Returns
        -------
        nothing
        '''
        p = Players()
        pf = Playfield()
        p1_name = p.startup(1)
        if fiend == "1":
            p2_name = p.startup(2)
        else:
            p2_name = "Herbert Tryhard"
        p_ID = 1
        p_name_cur = p1_name
        p_data = pf.playdata_init()
        pf.print_playfield(p_data)

        notfinished = True
        while notfinished:
            if p_ID == 3:
                selection = random.randint(0, 5)
            else:
                selection = p.player_move(p_name_cur)
            p_data = pf.play_data_update(selection, p_data, p_name_cur, p_ID)
            pf.cleansreen()
            pf.print_playfield(p_data)
            pf.winner_check(p_data, p_name_cur, p_ID)

            p_name_cur = p.player_change(p_ID, p1_name, p2_name)
            if p_ID == 1 and fiend == "1": #fiend == human
                p_ID = 2
            elif p_ID == 1 and fiend == "2": #fiend == AI
                p_ID = 3
            else:
                p_ID = 1




class Endgame():
    ''' checks after every move if game is won
        prints the screen for the winner
    '''
    def winselector(self, p_ID, p_name):
        '''selects the correct ending screen

        Parameters
        ----------
        p_ID: ID of actual player
        p_name: name of actual player

        Returns
        -------
        nothing
        '''
        if p_ID < 3:
            self.human_win(p_name)
        elif p_ID == 3:
            self.ai_win(p_name)
        else:
            self.draw()


    def newgame(self):
        '''asks player whether a new game shall be played or not

        Returns
        -------
        nothing
        '''
        g = Game()
        newgame = input(f'If you want to play another round enter y/Y, all other commands will quit >> ')
        if newgame == "y" or newgame == "Y":
            g.ai_vs_human()
        else:
            print(f'Thank you for playing!')
            exit()



    def human_win(self, p_name):
        '''ending screen when human player won
        Parameters
        ----------
        p_name: name of actual player

        Returns
        -------
        nothing
        '''
        print("******************************************\n"
        "CONGRATULATIONS", p_name, ", you won!\n"
        "******************************************\n")
        self.newgame()

    def ai_win(self, p_name):
        '''ending screen when ai won

        Parameters
        ----------
        p_name: name of ai

        Returns
        -------
        nothing
        '''
        print("******************************************\n"
        "I am sorry loser,", p_name, "won.\n"
        "******************************************\n")
        self.newgame()

    def draw(self):
        '''ending screen when draw (no winner)

        Returns
        -------
        nothing
        '''
        print("******************************************\n"
        "Oh no, there is no winner...\n"
        "******************************************\n")
        self.newgame()



if __name__ == '__main__':
    ''' runs the game
    '''
    g = Game()
    g.titlescreen()
    g.rules_set()
    g.ai_vs_human()


