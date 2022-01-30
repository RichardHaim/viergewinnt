from rules import *
from startup_screen import *
from end_screen import *
import os


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
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 0, 0, 0]  # bottom row
        ]
        return play_data



    def winner_check(self, p_data, p_name):
#TODO write winner check
# win = 4 in row; 4 in column, 4 diagonal
# needs to return: name of winner + call endgame

        pass



    def play_data_update(self, selected_field, p_data, p_name, p_ID):
        """Checks if selected column is free to select + places move

        Returns
        -------
        p_data
        p_move
        """

        # TODO 1) check, if selected column is free to select (max-row)
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
                if pos == 2:
                    playfield[playfield_row][playfield_pos] = "O"
                playfield_pos += 2
            playfield_row += 1
            playfield_pos = 1

        print("")
        for row in playfield:
            listToStr = ' '.join(map(str, row))
            print(listToStr)



    def cleansreen(self):
        clear = lambda: os.system('clear')
        clear()



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





class Endgame():
    ''' checks after every move if game is won
        prints the screen for the winner
    '''


class Game():
#TODO update comment section of this class
    ''' initializes the game
        gets playfield and players
        asks for moves and checks if moves are valid + changes player (AI if implemented)
        returns winner & asks for end/new start
    '''
    # sets the start of the round, player 1 will always start with token 1 = X, player 2 resumes with token 2 = O

#TODO aktiv setzen

    p = Players()
    pf = Playfield()
    pf.cleansreen()
    titlescreen()
    rules_set()
    p1_name = p.startup(1)
    p2_name = p.startup(2)
    p_ID = 1
    p_name_cur = p1_name



    def gameloop(self):
        p_data = self.pf.playdata_init()
        notfinished = True
        while notfinished:
            self.pf.cleansreen()
            self.pf.print_playfield(p_data)
            selection = self.p.player_move(self.p_name_cur)
            p_data = self.pf.play_data_update(selection, p_data, self.p_name_cur, self.p_ID)
            self.p_name_cur = self.p.player_change(self.p_ID, self.p1_name, self.p2_name)

#TODO put here win-check

            if self.p_ID == 1:
                self.p_ID = 2
            else:
                self.p_ID = 1

# HIER ENDET DIE SCHLEIFE !
            #notfinished = not notfinished





if __name__ == '__main__':
    ''' starts the game
    '''
    g = Game()
    g.gameloop()


