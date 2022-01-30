# Design
Description of implementation
## How we implemented the startup of the game
- The titlescreen had to be as simple as possible so we did that with a simple print function and implemented it to the main file.
- The playercheck has been implemented also with a simple input function because its easy to use, easy to understand for the player and also not hard to code for us.
- The playercheck has been implemented also with a simple input function because its easy to use, easy to understand for the player. By pressing "1" you'll be playing against AI and by pressing "2" you'll be playing against another player.
- For clarification, which player begins, next move etc. you have to put in your name. Meanwhile the game it shows your name when the player has to do a move and we will use it also for the end screen.
## Game itself
-  We decided to save the moves in a list with 0, 1, 2 (empty, player 1 and player 2/AI) because it was easier for us to handle if it was a hit or no hit. 
-  We decided to create a list called "playfield" that is purely used for printing the play_data in convenient format, the information of play_data is routed through for loop to correctly populate playfield with "X", "O" and empty.
## After the game
-  After checking who won the game we needed a end screen. For winner, loser and draw screen, we wanted to make a single screen for these in a additional file because we didn't want to litter our main file. One screen if a player wins, one if the AI wins and another one if its a draw. After the screen, the player has the opportunity to start a new game or exit. We solved that with impleneting the main file.
