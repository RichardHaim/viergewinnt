# Design
Description of implementation
## Startup of the game
- The titlescreen had to be as simple as possible so we did that with a simple print function and implemented it to the main file.
- At startup the game asks if you want to play against another human or AI. This has been implemented with a function named "ai_vs_human". By pressing "2" you'll be playing against AI and by pressing "1" you'll be playing against another human player.
- For clarification, which player begins and next move etc., the program aks you for your name. Over the whole game, the name of the player which has to do a move is shown. We also used the variable for the end screen to show which player has won the game. We assigned player 1 with "X" and player 2 with "O".  
- For getting the rules of the game, we created "ruleset" which shows by every start of the game the rules of the game.
## Game itself
-  to set up a move for the game, we added a input for "player_moves" + an validation check, which checks if the moves are valid or not. (e.g. you cannot place a playerblock on a field which is already taken
-  We decided to save the moves in a list with 0, 1, 2 and 3 (empty=0, player 1=1, player 2=2 and 3 = AI) because it was easier for us to handle if it was a hit or a no hit. 
-  We decided to create a list called "print_playfield" that is purely used for printing the "play_data" in convenient format, the information of play_data is routed through a "for loop" to correctly populate the playfield with "X", "O" and "empty".
- Our computer opponent, called "Herbert Tryhard", is a simple KI which places its moves by creating a random number which runs through validation check and then places the move on the playfield.
## After the game
-  After checking who won the game we needed an end screen. One screen if a player wins, one if the AI wins and another one if its a draw. After the screen, the player has the opportunity to start a new game by pressing "Y", any other key will exit the game. 
-  If it's a draw, another end screen will be shown.
