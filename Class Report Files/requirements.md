# Requirements
A Software Requirements Specification (SRS) is a written understanding of system requirements prior to any actual design or implementation work. The SRS document states in precise and explicit language those functions and capabilities a software system must provide, and any required constraints which the system must follow. An SRS contains functional and nonfunctional requirements only, rather than design ideas.

## Functional requirements

1. Software must access users previously played games through chess.com public API.
   Evaluation method: If the software asks for the persons chess.com username and month they want to access and then uses their games for the rest of the implementation then this has been met.
   Dependency: Tehnically none, I can do everything else without having imported a users games, but really all of the functional requirements depend on this one.
   Priority: middle
   Requirement revision history: week 5, have done preliminary research on the API and how it works, also small tests, did this to be able to understand if the project is possible. 

2. Software must use stockfish to analyse the previously played games finding the weak moves played.
   Evaluation Method: Since this will be the only way to analyse games, if their is any proof of analysis of the chess game this has been completed. 
   Dependency: 3
   Priority: essential
   Requirement revision history: Week 5, looked at documentation to get a sense of what is possible. 

3. Software must give the user the opportunity to play a stronger move from a position in the list of positions that they played weak moves. 
   Evaluation Method: If the program gives the user a prompt to make a better move, and has the power to input and parse users move then this requirement has been met. 
   Dependency: 4
   Priority: essential
   Requirement revision history: None

4. Software must give feedback on the users new move using stockfish for analysis. 
   Evaluation Method: If the program offers feedback on the move the user plays like, "great move" or "there is a better move" or "you played the best move" etc. 
   Dependency: 5
   Priority: essential
   Requirement revision history: None 

5. Software must change the list of positions of weak moves if the user has played a strong move. 
   Evaluation Method: This would have to be looked at in the code or by tracking the variables as they change. 
   Dependency: none
   Priority: high
   Requirement revision history: none

6. Software can save a users previous data
   Evaluation Method: If you can stop the program and restart it and end up in the same data without reuploading the games played. 
   Dependency: none
   Priority: if time permits
   Requirement revision history: none

7. Software has a functional visual chess board with pieces that can move
   Evaluation Method: how do you make moves? if it is with a visualized chess board this requirment is completed
   Dependency: none
   Priority: low
   Requirement revision history: none

## Non-functional requirements
Qualities or constraints that the software must have or comply with, but which are not operations that will be automated.

1. Software must use python
   Evaluation Method: is it written in python? if yes then this requirement is completed.
   Dependency: all of them
   Priority: essential 
   Requirement revision history: years of coding in python from freshman until today
