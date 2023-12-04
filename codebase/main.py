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


def import_games(month, year, username):
    # This gets the users data from the Chess.com server
    txt = urlopen(f"https://api.chess.com/pub/player/{username}/games/{year}/{month}/pgn")
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
        stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        for r in range(len(games[i])):
            previousval = stockfish.get_evaluation()["value"]
            board.push_san(games[i][r])
            stockfish.set_fen_position(board.fen())
            newval = stockfish.get_evaluation()["value"]
            if r % 2 == 0:
                # White move
                score = newval - previousval
                if score < -100:
                    weak_moves.append((i, r, score))
            else:
                score = newval - previousval
                if score > 100:
                    weak_moves.append((i, r, score))

    return weak_moves


cleanedgames = [['e4', 'd5', 'e5', 'e6', 'd4', 'Nc6', 'c3', 'Nge7', 'Bd3', 'g6', 'Nf3', 'Bg7', 'Bg5', 'h6', 'Bf6', 'Bxf6', 'exf6', 'Nf5', 'Bxf5', 'exf5', 'Qe2+', 'Be6', 'Na3', 'Qxf6', 'Nb5', 'O-O-O', 'Ne5', 'h5', 'Nxc6', 'bxc6', 'Nxa7+', 'Kb7', 'Nxc6', 'Kxc6', 'a4', 'Bd7', 'Qb5+', 'Kd6', 'Qc5+', 'Ke6', 'Kf1', 'Rc8', 'Re1+', 'Qe5', 'Rxe5+', 'Kf6', 'Qxd5', 'Bxa4', 'g3', 'Rb8', 'Kg2', 'Rb5', 'Qc6+', 'Kg5', 'Rxb5', 'Rb8', 'c4', 'Bxb5', 'cxb5', 'Rc8', 'h4+', 'Kg4', 'd5', 'g5', 'hxg5', 'Kxg5', 'd6', 'Rd8', 'Qxc7', 'Re8', 'd7'], ['Nf3', 'd5'], ['e4', 'c6', 'd4', 'd5', 'Nc3', 'Nf6', 'e5', 'Nfd7', 'Nf3', 'e6', 'Bg5', 'Be7', 'h4', 'c5', 'Bb5', 'O-O', 'a3', 'cxd4', 'Nxd4', 'Nc5', 'b4', 'Ne4', 'Nxe4', 'dxe4', 'f3', 'e3', 'g3', 'Bxg5', 'hxg5', 'Qxg5', 'Qd3', 'Qxg3+', 'Ke2', 'Qf2+', 'Kd1', 'Bd7', 'Qxh7#']]
weak_moves = [(0, 14, -189), (0, 30, -136), (0, 35, 280), (0, 40, -427), (0, 41, 674), (0, 46, -162), (0, 51, 109), (0, 55, 2676), (0, 56, -2727), (0, 59, 1550), (0, 60, -461), (2, 14, -132), (2, 19, 159), (2, 24, -157), (2, 25, 151), (2, 26, -131), (2, 32, -215), (2, 35, 297)]

print(weak_moves)
print(cleanedgames)

answer = "y"
while(answer == "y"):
    quiz = random.choice(weak_moves)
    print(quiz)
    if quiz[1] % 2 == 0:
        print("White played " + cleanedgames[quiz[0]][quiz[1]] + " find a better move.")
    else:
        print("Black played " + cleanedgames[quiz[0]][quiz[1]] + " find a better move.")

    board = chess.Board()
    for i in range(0, quiz[1]):
        board.push_san(cleanedgames[quiz[0]][i])

    stockfish.set_fen_position(board.fen())
    pre_val = stockfish.get_evaluation()["value"]
    bestmove = stockfish.get_best_move()
    print(stockfish.get_board_visual())
    print(stockfish.get_best_move())



    done = False
    while (not done):
        new_move = input()
        try:
            board.push_san(new_move)
            new_val = stockfish.get_evaluation()["value"]
            print(quiz[2], pre_val, new_val)
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
            done = True
        except:
            print("Not a valid move. Try Again.")

    print("Would you like to do another one? (y or n)")
    answer = input()
