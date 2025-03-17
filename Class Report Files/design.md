### Design

## Description 
A python program that can pull someone's games played on chess.com, use stockfish to analyse the pulled games to find weak points in play, prompt the user to make a better move on a chessboard in the application, give feed back on the new move played so that the user can improve their chess game, and finally either get rid of the position if they played a strong move or keep it if they played a weak one. 

## Major software components 

### Methods
import(): this method imports the games given a username and a given month.  

analyse(): this method will analyse the games provided by a list of strings (games will be in PGN format) and return a list of weak moves from each of the games

quiz(): this method will choose a random weak point in play and prompt the user to make a better move. 

feedback(): this method will give feedback given a position and the move played. 

update(): given the result of the quiz, this method will update the list of weak points depending on the quality of move the user played. 

## Flow of control/data

The program will start by prompting the user to enter a chess.com username and a month of games to look at, after the user enters this data the program will analyse the games and create a list of weak points in the games. Then the user will be prompted to play a better move than before, after the move is played then the program will update it list of weak points if the user plays a good move. Afterwards, it should then ask the user if it would like to do a new instance, if yes they will be quizzed again. 




