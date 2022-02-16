# UnitTest
With the testfile we aim at testing the most basic functions of the code.

## Testcases and setup
### Player input
* test if the input given by the player/ai is correctly detected as valid/not valid move (method "play_data_update")
* test if the field chosen by the player is stored in the correct playce in play_data (method "player_move_validation")
* test if code detects that the selected column is _not full_ (method "play_data_validation")
* test if code detects that the selected column is _full_ (method "play_data_validation")

### Winner detection
* test if code detects the winner correctly (method "winner_validation")
* test if code detects draw correctly (method "winner_validation")

### setUp()
The setUp includes randomly created cases of "play_data" to make it possible for the testcases to verify correct behaviour.

## Coverage
The tests do not cover 100% of the code, but covers the most basic input/output methods to make sure, that the game is running without errors.