import re
import time
from urllib.request import urlopen
import chess
from stockfish import Stockfish
stockfish = Stockfish(path=r"C:\Users\bisterj\PycharmProjects\stockfish\stockfish-windows-x86-64-modern.exe")
stockfish.set_depth(20)
stockfish.set_skill_level(20)

# board = chess.Board()
# board.push_san("e4")
# board.push_san("e5")
#
# stockfish.set_fen_position(board.fen())
# print(stockfish.get_best_move())

# This gets the users data from the Chess.com server
txt = urlopen("https://api.chess.com/pub/player/jakeBeans/games/2023/05/pgn")
data = txt.read()
file = open("Games.pgn", "w")
file.writelines(data.decode("utf-8"))


def cleanfile(filename):
    file = open(filename, "r+")
    txt = file.readlines()
    clean = []
    for t in txt:
        # print(t[0])
        if t[0] == "1":
            clean.append(t)
    return clean


games = cleanfile("Games.pgn")
cleanedgames = []

for game in games:
    cleangame = re.sub(r' {[^}]*}', '', game) #found from google generative AI tool
    cleanedgames.append(cleangame)

for game in cleanedgames:

    moves = game.split()
    trash = []

    for move in moves:
        if "." in move:
            trash.append(move)
        elif "-" in move:
            trash.append(move)

    for t in trash:
        moves.remove(t)

    i = cleanedgames.index(game)
    cleanedgames.insert(i, moves)
    cleanedgames.remove(game)

board = chess.Board()
weak_moves = []

# for i in range(len(cleanedgames)):
i = 0
for r in range(len(cleanedgames[i])):
    previousval = stockfish.get_evaluation()["value"]
    board.push_san(cleanedgames[i][r])
    stockfish.set_fen_position(board.fen())
    newval = stockfish.get_evaluation()["value"]
    score = newval - previousval
    if score < -100:
        weak_moves.append((i, r, score))

print(weak_moves)



# previousval = stockfish.get_evaluation()["value"]
# board.push_san("h4")
# stockfish.set_fen_position(board.fen())
# newval = stockfish.get_evaluation()["value"]
# print(newval - previousval)
# print(stockfish.get_board_visual(True))




# print("hello welcome to the chess trainer.")
# print("what is your chess.com username?")
# username = input()
# print(f"hello {username}, what month would you like to look at? (Use numbers i.e. 04)")
# month = input()
# print("Getting your chess games from Chess.com...")
#
# # code goes here for pubAPI
#
# print(f"{username} would you like to train?")
# answer = input()
#
# # code here for presenting a chess problem
#
# print("Chess position")
# print("Make your move:")
# move = input()
# print("analysing your move...")
# time.sleep(1)
# print("Good Job! That was a great move!")

