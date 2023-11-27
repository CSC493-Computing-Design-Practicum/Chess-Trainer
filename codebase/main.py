import re
from urllib.request import urlopen
import chess
import random
from stockfish import Stockfish
stockfish = Stockfish(path=r"C:\Users\bisterj\PycharmProjects\stockfish\stockfish-windows-x86-64-modern.exe")
stockfish.set_depth(20)
stockfish.set_skill_level(20)


def cleanfile(filename):
    file = open(filename, "r+")
    txt = file.readlines()
    clean = []
    for t in txt:
        if t[0] == "1":
            clean.append(t)
    return clean


def import_games(month, year):
    # This gets the users data from the Chess.com server
    txt = urlopen(f"https://api.chess.com/pub/player/jakeBeans/games/{year}/{month}/pgn")
    data = txt.read()
    file = open("Games.pgn", "w")
    file.writelines(data.decode("utf-8"))

    file = open("Games.pgn", "r+")
    games = cleanfile("Games.pgn")
    cleanedgames = []

    for game in games:
        cleangame = re.sub(r' {[^}]*}', '', game)  # found from google generative AI tool
        cleanedgames.append(cleangame)

    for game in cleanedgames:

        moves = game.split()
        trash = []

        for move in moves:
            if "." in move:
                trash.append(move)
            # this part fixes the illegal move problem before took out all castling since
            # I removed all moves with "-" i.e. O-O is a valid move.
            elif move == "0-1" or move == "1-0":
                trash.append(move)

        for t in trash:
            moves.remove(t)

        i = cleanedgames.index(game)
        cleanedgames.insert(i, moves)
        cleanedgames.remove(game)
    return cleanedgames


def analyse(games):
    board = chess.Board()
    weak_moves = []

    for i in range(len(games)):
        board.set_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        for r in range(len(games[i])):
            previousval = stockfish.get_evaluation()["value"]
            board.push_san(games[i][r])
            stockfish.set_fen_position(board.fen())
            newval = stockfish.get_evaluation()["value"]
            if r % 2 == 0:
                score = newval - previousval
            else:
                score = -(newval - previousval)
            if score < -100:
                if r % 2 == 0:
                    weak_moves.append((i, r, score))
                else:
                    weak_moves.append((i, r, -score))

    return weak_moves


cleanedgames = import_games(10, 2023)
weak_moves = analyse(cleanedgames)

print(weak_moves)

answer = "y"
while(answer == "y"):
    quiz = random.choice(weak_moves)
    print(quiz)
    if quiz[1] % 2 == 0:
        print("White played " + cleanedgames[quiz[0]][quiz[1]] + " find a better move.")
    else:
        print("Black played" + cleanedgames[quiz[0]][quiz[1]] + " find a better move.")

    board = chess.Board()
    for i in range(0, quiz[1]):
        board.push_san(cleanedgames[quiz[0]][i])

    pre_val = stockfish.get_evaluation()["value"]
    stockfish.set_fen_position(board.fen())
    bestmove = stockfish.get_best_move()
    print(stockfish.get_board_visual())

    new_move = input()

    try:
        board.push_san(new_move)
        new_val = stockfish.get_evaluation()["value"]
        new_score = new_val - pre_val

        if new_score > quiz[2]:
            print("This is a better move")
            if new_score > 0:
                print("This was a good move.")
            elif new_score > -100:
                print("This was an okay move.")
            else:
                print("But, this was not a good move.")
            weak_moves.remove(quiz)
        else:
            print("This was not a better move.")

        print("The best move was " + bestmove)
    except:
        print("Not a valid move.")

    print("Would you like to do another one? (y or n)")
    answer = input()
