# Requirements
A Software Requirements Specification (SRS) is a written understanding of system requirements prior to any actual design or implementation work. The SRS document states in precise and explicit language those functions and capabilities a software system must provide, and any required constraints which the system must follow. An SRS contains functional and nonfunctional requirements only, rather than design ideas.

## Functional requirements

Software must access users previously played games through chess.com public API. 

Software must use stockfish to analyse the previously played games. 

Software must use analysed games to find positions where the player has played weak moves. 

Software must give the user the opportunity to play a stronger move from a position in the list of positions that they played weak moves. 

Software must give feedback on the users new move using stockfish for analysis. 

Software must change the list of positions of weak moves if the user has played a strong move. 

## Non-functional requirements
Qualities or constraints that the software must have or comply with, but which are not operations that will be automated.

Software must use python
