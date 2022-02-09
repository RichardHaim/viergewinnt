import unittest
import viergewinnt.main
#import viergewinnt.rules
#import viergewinnt.startup_screen
vgP = viergewinnt.main.Playfield()

class Testcase(unittest.TestCase):
    def setUp(self):
        self.inputcheck1 = "1" #valid input
        self.inputcheck1_out = [[0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [1, 0, 0, 0, 0, 0]  # bottom row
        ]
        self.inputcheck2 = "2" #valid input
        self.inputcheck2_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 1, 0, 0, 0, 0]  # bottom row
        ]
        self.inputcheck3 = "3" #valid input
        self.inputcheck3_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 1, 0, 0, 0]  # bottom row
        ]
        self.inputcheck4 = "4" #valid input
        self.inputcheck4_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 1, 0, 0]  # bottom row
        ]
        self.inputcheck5 = "5" #valid input
        self.inputcheck5_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 0, 1, 0]  # bottom row
        ]
        self.inputcheck6 = "6" #valid input
        self.inputcheck6_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 0, 0, 1]  # bottom row
        ]

        self.isfullcheck1 = 1
        self.isfullcheck2 = 2
        self.isfullcheck3 = 3
        self.isfullcheck4 = 4
        self.isfullcheck5 = 5
        self.isfullcheck6 = 6

        self.winner_in_row1 = [ #winner == true
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [1, 1, 1, 1, 0, 0]  # bottom row
        ]
        self.winner_in_row2 = [ #winner == true
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 1, 1, 1, 1],  # row 2
            [1, 1, 1, 2, 2, 2]  # bottom row
        ]
        self.winner_in_col1 = [ #winner == true
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [1, 0, 0, 0, 0, 0],  # row 4
            [1, 0, 0, 0, 0, 0],  # row 3
            [1, 0, 0, 0, 0, 0],  # row 2
            [1, 0, 0, 0, 0, 0]  # bottom row
        ]
        self.winner_in_col2 = [ # winner == true
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 1, 0, 0, 0, 0],  # row 4
            [0, 1, 0, 1, 0, 0],  # row 3
            [0, 1, 0, 1, 0, 0],  # row 2
            [0, 1, 0, 1, 0, 0]  # bottom row
        ]
        self.winner_dia_r_to_l1 = [ # winner == true
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 1, 0, 0],  # row 4
            [0, 0, 1, 2, 0, 0],  # row 3
            [0, 1, 2, 2, 0, 0],  # row 2
            [1, 2, 2, 2, 0, 0]  # bottom row
        ]
        self.winner_dia_r_to_l2 = [ #winner == true
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 1],  # row 5
            [0, 0, 0, 0, 1, 1],  # row 4
            [0, 0, 0, 1, 2, 1],  # row 3
            [0, 0, 1, 2, 1, 2],  # row 2
            [0, 0, 2, 2, 2, 1]  # bottom row
        ]
        self.winner_dia_l_to_r1 = [ #winner == true
            [0, 0, 0, 0, 0, 0],  # row 7
            [1, 0, 0, 0, 0, 0],  # row 6
            [0, 1, 0, 0, 0, 0],  # row 5
            [0, 2, 1, 0, 0, 0],  # row 4
            [0, 1, 2, 1, 0, 0],  # row 3
            [0, 1, 1, 2, 0, 0],  # row 2
            [0, 1, 2, 2, 0, 0]  # bottom row
        ]
        self.winner_dia_l_to_r2 = [ #winner == true
            [0, 0, 1, 0, 0, 0],  # row 7
            [0, 0, 1, 1, 0, 0],  # row 6
            [0, 0, 1, 2, 1, 0],  # row 5
            [0, 0, 2, 2, 1, 1],  # row 4
            [0, 0, 2, 1, 2, 2],  # row 3
            [0, 0, 1, 1, 2, 1],  # row 2
            [0, 0, 1, 2, 2, 1]  # bottom row
        ]
        self.winner_draw_isfull = [
            [1, 2, 1, 2, 1, 2],  # row 7
            [2, 1, 2, 1, 2, 1],  # row 6
            [2, 1, 2, 1, 2, 1],  # row 5
            [2, 1, 2, 1, 2, 1],  # row 4
            [1, 2, 1, 2, 1, 2],  # row 3
            [1, 2, 1, 2, 1, 2],  # row 2
            [1, 2, 1, 2, 1, 2]  # bottom row
        ]


    def testinput(self):
        self.assertEqual(self.inputcheck1_out, vgP.play_data_update(self.inputcheck1, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck2_out, vgP.play_data_update(self.inputcheck2, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck3_out, vgP.play_data_update(self.inputcheck3, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck4_out, vgP.play_data_update(self.inputcheck4, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck5_out, vgP.play_data_update(self.inputcheck5, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck6_out, vgP.play_data_update(self.inputcheck6, vgP.playdata_init(), "player", 1))

        self.assertEqual(f'Column {self.isfullcheck1} is full and cannot be selected',
                         vgP.play_data_update(self.isfullcheck1, self.winner_draw_isfull, "player", 1))
        self.assertEqual(f'Column {self.isfullcheck2} is full and cannot be selected',
                         vgP.play_data_update(self.isfullcheck2, self.winner_draw_isfull, "player", 1))
        self.assertEqual(f'Column {self.isfullcheck3} is full and cannot be selected',
                         vgP.play_data_update(self.isfullcheck3, self.winner_draw_isfull, "player", 1))
        self.assertEqual(f'Column {self.isfullcheck4} is full and cannot be selected',
                         vgP.play_data_update(self.isfullcheck4, self.winner_draw_isfull, "player", 1))
        self.assertEqual(f'Column {self.isfullcheck5} is full and cannot be selected',
                         vgP.play_data_update(self.isfullcheck5, self.winner_draw_isfull, "player", 1))
        self.assertEqual(f'Column {self.isfullcheck6} is full and cannot be selected',
                         vgP.play_data_update(self.isfullcheck6, self.winner_draw_isfull, "player", 1))

        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_in_row1, "player", 1))
        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_in_row2, "player", 1))
        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_in_col1, "player", 1))
        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_in_col2, "player", 1))
        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_dia_l_to_r1, "player", 1))
        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_dia_l_to_r2, "player", 1))
        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_dia_r_to_l1, "player", 1))
        self.assertIn("CONGRATULATIONS", vgP.winner_check(self.winner_dia_r_to_l2, "player", 1))

        self.assertIn("Oh no", vgP.winner_check(self.winner_draw_isfull, "player", 1))


if __name__ == '__main__':
    unittest.main()