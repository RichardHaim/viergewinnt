# Design
Description of implementation

## How we implemented the startup of the game
- The titlescreen had to be as simple as possible so we did that with a simple print function and implemented it to the main file.
- The playercheck has been implemented also with a simple input function because its easy to use, easy to understand for the player and also not hard to code for us.
## Game itself
-  We decided to save the moves in a list with 0, 1, 2 (empty, player 1 and player 2/AI) because it was easier for us to handle if it was a hit or no hit. 
-....

## After the game
-  After checking who won the game we needed a end screen. For winner, loser and draw screen, we wanted to make a single screen for these in a additional file because we didn't want to litter our main file. One screen if a player wins, one if the AI wins and another one if its a draw. After the screen, the player has the opportunity to start a new game or exit. We solved that with impleneting the main file.

