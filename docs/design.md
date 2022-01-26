# Design
Description of implementation
## How we implemented the startup of the game
- The titlescreen had to be as simple as possible so we did that with a simple print function and implemented it to the main file.
- The "playercheck" has been implemented also with a simple input function because its easy to use and easy to understand for the player. By pressing "1" you'll be playing against AI and by pressing "2" you'll be playing against another player.
- For clarification, which player begins, next move etc. you have to put in your name. Meanwhile the game, the name of the player which has to do a move is shown. We also use the variable for the end screen to show which player has won the game. 
- For getting the rules of the game, we created "ruleset" which shows, by every start of the game the rules of the game.
## Game itself
-  to set up a move for the game, we added a input for "player_moves" + an validation checks, which checks if the moves are valid or not. (e.g. you cannot place a playerblock on a field which is already taken
-  We decided to save the moves in a list with 0, 1, 2 (empty, player 1 and player 2/AI) because it was easier for us to handle if it was a hit or no hit. 
-  We decided to create a list called "playfield_init" that is purely used for printing the "play_data" in convenient format, the information of play_data is routed through for loop to correctly populate playfield with "X", "O" and empty.
- "play_data" checks, which fields are already set up and which are not and we implemented it to "the_game" where we moved additional code for the main game, also not to litter our main file and brings more structure to the code itself.
## After the game
-  After checking who won the game we needed a end screen. For winner, loser and draw screen, we wanted to make a single screen for these in a additional file because we didn't want to litter our main file. One screen if a player wins, one if the AI wins and another one if its a draw. After the screen, the player has the opportunity to start a new game or exit. We solved that with impleneting the main file.
