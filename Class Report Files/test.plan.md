# Testing Plan

## Summary
Testing will be done throughout the implementation of each new compenent. The way this testing will look is that usually I will write out the whole implementation as I think it should look and then run my code to see if it works as intended. In most cases I get some runtime errors or the code does not work as expected so I do some debugging just to an implmentation that will run as expected on the most general of my test cases. Then once that runs as expected I will start testing different edge cases and seeing if they come up with the expected result. If they do, go on to the next edge case, otherwise fix the implementation until it does run as expected, and then move on to another edge case. Once, I can't think of any more edge cases to test, I deem the component completed and commit and push to github. 

A unique name and number (which may be related to the requirement number, but are typically not identical.

The specific requirement that this Test Case is intended to test.

Preconditions which detail which state of the software needs to be in to exercise the Test Case (sometimes this is a previous Test Case that must always be run before the current Test Case.)

Steps that describe the specific steps that make up the interaction with the software to run the Test Case

The desired results that describe the desired state of the software after the Test Case is executed successfully

## Key Test Cases
-#1 Public API call to chess.com, nothing else needs to work to test this case, if working should be able to pull someone's previously played games from chess.com into the developement environment

-#2 Cleaning the files imported from Chess.com, #1 needs to work to test this feature, If working the reult of the cleaning should be just algebraic notation moves for each game played in the specified month. (e4, e5, Nf3, ...)

#3 Analysis of games for weak moves, all previous test cases need to be working, If working the result will be a list of weak moves including the index of the game it comes from, the index of the move being deemed weak and the score assigned to the move, this should be close if not exactly the same to the analysis from Chess.com's game report, or Lichess's analyzing equivalent. 

#4 Present a weak move to the user, all previous tests must be completed, If working it should show the user a ASCII chess board with the position laid out and prompt the user to make a better move. 

#5 Give feedback on the move played by the user, all previous tests are required to be completed before this can be tested, if working this should give the user feedback on how good the move was and if the move was better than the previously played move
