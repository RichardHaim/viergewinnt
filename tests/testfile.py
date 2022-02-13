import unittest
import viergewinnt.main as vg
vgP = vg.Playfield()
vgPs = vg.Players()

class Testcase(unittest.TestCase):
    def setUp(self):
        self.inputcheck1 = 1 #valid input
        self.inputcheck1_out = [[0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [1, 0, 0, 0, 0, 0]  # bottom row
        ]
        self.inputcheck2 = 2 #valid input
        self.inputcheck2_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 1, 0, 0, 0, 0]  # bottom row
        ]
        self.inputcheck3 = 3 #valid input
        self.inputcheck3_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 1, 0, 0, 0]  # bottom row
        ]
        self.inputcheck4 = 4 #valid input
        self.inputcheck4_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 1, 0, 0]  # bottom row
        ]
        self.inputcheck5 = 5 #valid input
        self.inputcheck5_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 0, 1, 0]  # bottom row
        ]
        self.inputcheck6 = 6 #valid input
        self.inputcheck6_out = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [0, 0, 0, 0, 0, 0],  # row 6
            [0, 0, 0, 0, 0, 0],  # row 5
            [0, 0, 0, 0, 0, 0],  # row 4
            [0, 0, 0, 0, 0, 0],  # row 3
            [0, 0, 0, 0, 0, 0],  # row 2
            [0, 0, 0, 0, 0, 1]  # bottom row
        ]
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
        self.winner_dia_r_to_l2 = [ # winner == true
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
        self.is_not_full = [
            [0, 0, 0, 0, 0, 0],  # row 7
            [2, 1, 2, 1, 2, 1],  # row 6
            [2, 1, 2, 1, 2, 1],  # row 5
            [2, 1, 2, 1, 2, 1],  # row 4
            [1, 2, 1, 2, 1, 2],  # row 3
            [1, 2, 1, 2, 1, 2],  # row 2
            [1, 2, 1, 2, 1, 2]  # bottom row
        ]
        self.is_not_full_line = 0
        self.isfullcheck1 = 1
        self.isfullcheck2 = 2
        self.isfullcheck3 = 3
        self.isfullcheck4 = 4
        self.isfullcheck5 = 5
        self.isfullcheck6 = 6

        self.playermove_correct1 = "1"
        self.playermove_correct2 = "2"
        self.playermove_correct3 = "3"
        self.playermove_correct4 = "4"
        self.playermove_correct5 = "5"
        self.playermove_correct6 = "6"
        self.playermove_incorrect1 = "bla"
        self.playermove_incorrect2 = "44"
        self.playermove_incorrect3 = "234"
        self.playermove_incorrect4 = "0"


    def testinput(self):
        # test if field input is put into correct playce in play_data
        self.assertEqual(self.inputcheck1_out, vgP.play_data_update(self.inputcheck1, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck2_out, vgP.play_data_update(self.inputcheck2, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck3_out, vgP.play_data_update(self.inputcheck3, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck4_out, vgP.play_data_update(self.inputcheck4, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck5_out, vgP.play_data_update(self.inputcheck5, vgP.playdata_init(), "player", 1))
        self.assertEqual(self.inputcheck6_out, vgP.play_data_update(self.inputcheck6, vgP.playdata_init(), "player", 1))

        # test if player input is detected as correct/incorrect
        self.assertTrue(vgPs.player_move_validation(self.playermove_correct1))
        self.assertTrue(vgPs.player_move_validation(self.playermove_correct2))
        self.assertTrue(vgPs.player_move_validation(self.playermove_correct3))
        self.assertTrue(vgPs.player_move_validation(self.playermove_correct4))
        self.assertTrue(vgPs.player_move_validation(self.playermove_correct5))
        self.assertTrue(vgPs.player_move_validation(self.playermove_correct6))
        self.assertFalse(vgPs.player_move_validation(self.playermove_incorrect1))
        self.assertFalse(vgPs.player_move_validation(self.playermove_incorrect2))
        self.assertFalse(vgPs.player_move_validation(self.playermove_incorrect3))
        self.assertFalse(vgPs.player_move_validation(self.playermove_incorrect4))

        # test if code detects that selected column is not full
        self.assertTrue(vgP.play_data_validation(self.is_not_full_line,self.isfullcheck1,self.is_not_full))
        self.assertTrue(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck2, self.is_not_full))
        self.assertTrue(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck3, self.is_not_full))
        self.assertTrue(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck4, self.is_not_full))
        self.assertTrue(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck5, self.is_not_full))
        self.assertTrue(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck6, self.is_not_full))

        # test if code detects that selected column is full
        self.assertFalse(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck1, self.winner_draw_isfull))
        self.assertFalse(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck2, self.winner_draw_isfull))
        self.assertFalse(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck3, self.winner_draw_isfull))
        self.assertFalse(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck4, self.winner_draw_isfull))
        self.assertFalse(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck5, self.winner_draw_isfull))
        self.assertFalse(vgP.play_data_validation(self.is_not_full_line, self.isfullcheck6, self.winner_draw_isfull))

        # test if code detects winner
        self.assertEqual(1, vgP.winner_validation(1, self.winner_in_row1))
        self.assertEqual(1, vgP.winner_validation(1, self.winner_in_row2))
        self.assertEqual(1, vgP.winner_validation(1, self.winner_in_col1))
        self.assertEqual(1, vgP.winner_validation(1, self.winner_in_col2))
        self.assertEqual(1, vgP.winner_validation(1, self.winner_dia_l_to_r1))
        self.assertEqual(1, vgP.winner_validation(1, self.winner_dia_l_to_r2))
        self.assertEqual(1, vgP.winner_validation(1, self.winner_dia_r_to_l1))
        self.assertEqual(1, vgP.winner_validation(1, self.winner_dia_r_to_l2))

        # test if code detects draw
        self.assertEqual(99, vgP.winner_validation(1, self.winner_draw_isfull))


if __name__ == '__main__':
    unittest.main()