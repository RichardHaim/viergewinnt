from rules import *
from startup_screen import *
import random
from os import system, name


class Playfield():
    ''' initializes the playfield
        prints the playfield
        updates the played moves
    '''

    def playdata_init(self):
        play_data = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 1, 2],  # row 3
            [0, 0, 0, 1, 2, 2],  # row 2
            [0, 0, 2, 2, 1, 2]  # bottom row
        ]
        return play_data




    def winner_check(self, p_data, p_name, p_ID):
        '''checks after every move if game is won/draw
        '''

        eg = Endgame()

        # check 4 in row
        row = 0
        while row <= 6:
            col = 0
            while col <= 2:
                if (p_data[row][col] == p_ID and p_data[row][col+1] == p_ID and
                p_data[row][col+2] == p_ID and p_data[row][col+3] == p_ID):
                    eg.winselector(p_ID, p_name)
                col += 1
            row +=1

        # check 4 in column
        col = 0
        while col <= 5:
            row = 0
            while row <= 3:
                if (p_data[row][col] == p_ID and p_data[row+1][col] == p_ID and
                p_data[row+2][col] == p_ID and p_data[row]+3[col] == p_ID):
                    eg.winselector(p_ID, p_name)
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
                    if (p_data[row][col] == p_ID and p_data[row+1][col+1] == p_ID
                     and p_data[row+2][col+2] == p_ID and p_data[row+3][col+3] == p_ID):
                        eg.winselector(p_ID, p_name)
                    col += 1
                if (p_data[row][col] == p_ID and p_data[row + 1][col - 1] == p_ID
                        and p_data[row + 2][col - 2] == p_ID and p_data[row + 3][col - 3] == p_ID):
                    eg.winselector(p_ID, p_name)
                col += 1
            row += 1




    def play_data_update(self, selected_field, p_data, p_name, p_ID):
        """Checks if selected column is free to select + places move

        Returns
        -------
        p_data
        p_move
        """

        notfinished = True
        while notfinished:
            line = 6
            while line >= 0:
                if p_data[line][selected_field-1] == 0:
                    p_data[line][selected_field-1] = p_ID
                    return p_data
                line -= 1
            print(f'Column {selected_field} is full and cannot be selected')
            selected_field = Players().player_move(p_name)



    def print_playfield(self, p_data):

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
        '''clears the playing field'''
        if name == "nt":
            _ = system('cls')
        else:
            _ = system('clear')



class Players():
#TODO update this comment below
    ''' asks for number of players >> only with AI implemented, otherwise automatically 2 players
        stores player names
        allocates player ID (1 and 2) to player name
        player moves
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
        '''gets input of desired move and validates, if input is correct.

        Parameters
        ----------
        p_name: name of actual player

        Returns
        -------
        field: the columns, the player places the token
        '''
        notfinished = True
        while notfinished:

            selected_field = input(f'\n{p_name}, enter the column you want to place your token or enter q/Q to quit >> ')
            if selected_field == "Q" or selected_field == "q":
                print("\nTHANK YOU FOR PLAYING")
                exit()
            try:
                selected_field = int(selected_field)
                if selected_field >= 1 and selected_field <= 6:
                    return selected_field
                else:
                    print(f'No valid input')
            except:
                print(f'No valid input')



            # try:
            #     selected_field = int(input(f'{p_name}, please enter the column you want to place your move (1 - 6): '))
            #     if selected_field >= 1 and selected_field <= 6:
            #         return selected_field
            #     else:
            #         print(f'No valid input')
            # except:
            #     print(f'No valid input')




class Game():
#TODO update comment section of this class
    ''' initializes the game
        gets playfield and players
        asks for moves and checks if moves are valid + changes player (AI if implemented)
        returns winner & asks for end/new start
    '''
    # sets the start of the round, player 1 will always start with token 1 = X, player 2 resumes with token 2 = O


    pf = Playfield()
    pf.cleansreen()
    titlescreen()
    rules_set()



    def ai_vs_human(self):
        dec = input(f'To play against an human opponent press 1, to play against the computer press 2. To exit press q/Q >> ')
        if dec == "q" or dec == "Q":
            print("\nGood Bye!")
            exit()
        elif dec == "1":
            self.gameloop()
        else:
            self.gameloop_ai()


    def gameloop_ai(self):
        # p_ID for AI = 3
        # p_ID for human = 1
        pass


    def gameloop(self):
        p = Players()
        pf = Playfield()
        p1_name = p.startup(1)
        p2_name = p.startup(2)
        p_ID = 1
        p_name_cur = p1_name
        p_data = pf.playdata_init()
        pf.print_playfield(p_data)

        notfinished = True
        while notfinished:
            selection = p.player_move(p_name_cur)
            p_data = pf.play_data_update(selection, p_data, p_name_cur, p_ID)
            pf.cleansreen()
            pf.print_playfield(p_data)
            pf.winner_check(p_data, p_name_cur, p_ID)

            p_name_cur = p.player_change(p_ID, p1_name, p2_name)
            if p_ID == 1:
                p_ID = 2
            else:
                p_ID = 1




class Endgame():
    ''' checks after every move if game is won
        prints the screen for the winner
    '''
    def winselector(self, p_ID, p_name):
        if p_ID < 3:
            self.human_win(p_name)
        elif p_ID == 3:
            self.ai_win(p_name)
        else:
            self.draw()


    def newgame(self):
        g = Game()
        newgame = input(f'If you want to play another round enter y/Y, all other commands will quit >> ')
        if newgame == "y" or newgame == "Y":
            g.ai_vs_human()
        else:
            print(f'Thank you for playing!')
            exit()



    def human_win(self, p_name):
        print("******************************************\n"
        "CONGRATULATIONS", p_name, ", you won!\n"
        "******************************************\n")
        self.newgame()

    def ai_win(self, p_name):
        print("******************************************\n"
        "I am sorry", p_name, ", the computer won.\n"
        "******************************************\n")
        self.newgame()

    def draw(self):
        print("******************************************\n"
        "Oh no, there is no winner...\n"
        "******************************************\n")
        self.newgame()



if __name__ == '__main__':
    ''' starts the game
    '''
    g = Game()
    g.ai_vs_human()


