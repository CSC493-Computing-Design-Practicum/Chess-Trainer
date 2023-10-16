import re
import time
from urllib.request import urlopen
import chess
import random
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
# txt = urlopen("https://api.chess.com/pub/player/jakeBeans/games/2023/05/pgn")
# data = txt.read()
# file = open("Games.pgn", "w")
# file.writelines(data.decode("utf-8"))
#
#
# def cleanfile(filename):
#     file = open(filename, "r+")
#     txt = file.readlines()
#     clean = []
#     for t in txt:
#         # print(t[0])
#         if t[0] == "1":
#             clean.append(t)
#     return clean
#
#
# games = cleanfile("Games.pgn")
# cleanedgames = []
#
# for game in games:
#     cleangame = re.sub(r' {[^}]*}', '', game) #found from google generative AI tool
#     cleanedgames.append(cleangame)
#
# for game in cleanedgames:
#
#     moves = game.split()
#     trash = []
#
#     for move in moves:
#         if "." in move:
#             trash.append(move)
#         elif "-" in move:
#             trash.append(move)
#
#     for t in trash:
#         moves.remove(t)
#
#     i = cleanedgames.index(game)
#     cleanedgames.insert(i, moves)
#     cleanedgames.remove(game)
#
# board = chess.Board()
#
# weak_moves = []
#
#
# for i in [0, 5, 6, 7]:
#     board.set_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
#     for r in range(len(cleanedgames[i])):
#         previousval = stockfish.get_evaluation()["value"]
#         board.push_san(cleanedgames[i][r])
#         stockfish.set_fen_position(board.fen())
#         newval = stockfish.get_evaluation()["value"]
#         score = newval - previousval
#         if score < -100:
#             weak_moves.append((i, r, score))

# these are just for the demo tomorrow so that we don't have to wait for the whole thing to load
weak_moves = [(0, 10, -196), (0, 16, -139), (0, 18, -285), (0, 22, -401), (0, 28, -459), (0, 30, -291), (0, 36, -119), (0, 38, -941), (0, 48, -141), (0, 52, -212), (0, 54, -2252), (5, 4, -103), (5, 12, -387), (6, 6, -454), (7, 0, -589), (7, 14, -129), (7, 16, -203), (7, 20, -408), (7, 26, -512), (7, 32, -223), (7, 42, -138), (7, 48, -166)]
cleanedgames = [['e4', 'c5', 'd4', 'd6', 'Nf3', 'e5', 'dxe5', 'dxe5', 'Qxd8+', 'Kxd8', 'Bg5+', 'f6', 'Bh4', 'g5', 'Bg3', 'b6', 'h4', 'g4', 'Nfd2', 'Nc6', 'f3', 'Nd4', 'fxg4', 'Nxc2+', 'Kd1', 'Nxa1', 'g5', 'fxg5', 'hxg5', 'Ne7', 'Bh4', 'Bg4+', 'Be2', 'Bxe2+', 'Kxe2', 'Rc8', 'g6', 'hxg6', 'Bf6', 'Rxh1', 'Bxe7+', 'Bxe7', 'Nc3', 'Bg5', 'Nf3', 'Bf6', 'Nd5', 'Bh8', 'Ng5', 'Rb1', 'Nf7+', 'Kd7', 'g4', 'Rxb2+', 'Kd1', 'Ke6', 'Nxh8', 'Rxh8', 'Nc7+', 'Kd7', 'Na6', 'Rh1#'], ['e4', 'e5', 'Nc3', 'Nf6', 'Bc4', 'Bb4', 'd3', 'Bg5', 'h6', 'Bh4', 'g5', 'Bg3', 'Nh5', 'Bxe5', 'Qe8', 'd4', 'Nc6', 'Qxh5', 'Nxe5', 'dxe5', 'Bxc3+', 'bxc3', 'Qxe5', 'Qxh6', 'Qxc3+', 'Kd1', 'Qxa1+', 'Kd2', 'Qd4+', 'Bd3', 'd5', 'Qxg5+', 'Qg7', 'Qxd5', 'Be6', 'Qxb7', 'Rab8', 'Qxc7', 'Rfc8', 'Qxa7', 'Ra8', 'Qb7', 'Rxa2', 'Qxc8+', 'Bxc8', 'Nf3', 'Ra3', 'e5', 'f6', 'exf6', 'Qxf6', 'g4', 'Qc3+', 'Ke3', 'Ba6', 'Ne5', 'Qc5+', 'Ke4', 'Qb4+', 'Ke3', 'Qc5+', 'Ke4', 'Bb7+', 'Kf4', 'Bxh1', 'Bc4+', 'Bd5', 'Bxd5+', 'Qxd5', 'c4', 'Qd4+', 'Kf5', 'Qxf2+', 'Ke4', 'Qe3+', 'Kf5', 'Ra5', 'Kf6', 'Qxe5+', 'Kg6', 'Qg5#'], ['e4', 'e5', 'Nf3', 'Nc6', 'Bc4', 'Nh6', 'd4', 'exd4', 'Nxd4', 'Nxd4', 'Qxd4', 'b6', 'Bxh6', 'gxh6', 'Bc5', 'Qd5', 'd6', 'Qxa8', 'Ba6', 'Qxd8+', 'Kxd8', 'Bxa6', 'Re8', 'Nc3', 'Bb4', 'Rae1', 'd5', 'exd5', 'Rxe1', 'Rxe1', 'Bxc3', 'bxc3', 'c5', 'a4', 'h5', 'c4', 'f5', 'f4', 'h4', 'g3', 'hxg3', 'hxg3', 'h5', 'Re5', 'h4', 'gxh4', 'Kc7', 'h5', 'Kd6', 'h6', 'b5', 'h7', 'bxa4', 'h8=Q', 'a3', 'Qf8+', 'Kc7', 'Qxc5+', 'Kd7', 'Qxa3', 'Kc7', 'c5', 'Kd7', 'c6+', 'Kc7', 'Qc5', 'Kb8', 'c7+', 'Ka8', 'Re8#'], ['e4', 'e5', 'Bc4', 'Nf6', 'Nc3', 'd6', 'Nd5', 'Be6', 'Nxf6+', 'Qxf6', 'd3', 'd5', 'Bb5+', 'Nc6', 'exd5', 'Bc5', 'Be3', 'Bxd5', 'Bxc5', 'Bxg2', 'Qd2', 'Bxh1', 'Bxc6', 'bxc6', 'Bxa7', 'Kb7', 'Qa5', 'Ra8', 'Qb4+', 'Kxa7', 'Ne2', 'Rhb8', 'Qc5+', 'Ka6', 'Rxh1', 'e4', 'dxe4', 'Qxb2+', 'Kd2', 'Qb4+', 'Qc3', 'Qxc3+', 'Nxc3', 'Rd8+', 'Ke3', 'c5', 'Rb1', 'Rdb8', 'Rg1', 'Ka5', 'Nd5', 'c6', 'Nc7', 'Ra7', 'Rxg7', 'Rxc7', 'Rxh7', 'Rb2', 'Kd2', 'Rxa2', 'e5', 'Re7', 'f4', 'Ra4', 'Rh4', 'c4', 'c3', 'Ra2+', 'Ke3', 'f6', 'Rh6', 'fxe5', 'f5', 'Rf7', 'Rxc6', 'Rxf5', 'Rc5+', 'Kb6', 'Rxc4', 'Rxh2', 'Ke4', 'Rf4+', 'Kd3', 'Rh3+', 'Kc2', 'Rf2+', 'Kb3', 'Kb5', 'Rb4+', 'Ka5', 'Kc4', 'Rf4+', 'Kc5', 'Rxb4', 'cxb4+', 'Ka6', 'b5+', 'Kb7', 'b6', 'e4', 'Kd4', 'e3', 'Kd3', 'Kxb6', 'Ke2', 'Kc5', 'Kd3', 'Kd5', 'Ke2', 'Ke4', 'Kf1', 'Rf3+', 'Ke2', 'Rf2+', 'Ke1', 'Kf3', 'Kd1', 'e2+', 'Ke1', 'Rf1+', 'Kd2'], ['e4', 'e5', 'Nf3', 'Nc6', 'Nc3', 'Nf6', 'd4', 'd6', 'dxe5', 'dxe5', 'Bc4', 'Qxd1+', 'Nxd1', 'Nxe4', 'Be6', 'Bd3', 'Bc5', 'Bxe4', 'Nc3', 'f5', 'Bxc6', 'bxc6', 'Nxe5', 'Rhe8', 'Nxc6', 'Rd6', 'Ne5', 'Bd4', 'Nf7', 'Bxf7', 'Bf4', 'Rd7', 'Rad1', 'Bxc3', 'bxc3', 'Red8', 'Rb1', 'Bxa2', 'Ra1', 'Bc4', 'Rfb1', 'h6', 'Rxa7', 'Rd1+'], ['e4', 'e5', 'Nf3', 'Bc5', 'Bc4', 'd6', 'd3', 'Nc6', 'Ng5', 'Nb4', 'Nxf7', 'Qf6', 'Nxh8', 'Qxf2#'], ['e4', 'd5', 'exd5', 'Qxd5', 'Nc3', 'Qc6', 'd4', 'Na6', 'Bb5', 'Qxb5', 'Nxb5'], ['g3', 'e5', 'Bg2', 'Nf6', 'h3', 'd5', 'e3', 'g5', 'b3', 'h5', 'Bb2', 'Nc6', 'a3', 'b5', 'd4', 'g4', 'hxg4', 'Bxg4', 'f3', 'Bf5', 'e4', 'dxe4', 'dxe5', 'Nd5', 'fxe4', 'Bg4', 'Qd2', 'Bh6', 'Qxd5', 'Qxd5', 'exd5', 'Ne7', 'e6', 'Rg8', 'd6', 'cxd6', 'Bxa8', 'fxe6', 'Nc3', 'd5', 'Nxb5', 'e5', 'Nxa7', 'd4', 'Ne2', 'Bxe2', 'Kxe2', 'Kd7', 'Rhf1', 'Rxa8', 'Nb5', 'Nc6', 'Rf5', 'Re8', 'Rxh5', 'Bg7', 'Rh7', 'Re7', 'c3', 'Bf6', 'Rxe7+', 'Kxe7', 'cxd4', 'exd4', 'Nc7', 'Ne5'], ['e4', 'g6', 'd4', 'Bg7', 'Nf3', 'h6', 'Bc4', 'b6', 'Nc3', 'Bb7', 'd5', 'a6', 'Bf4', 'd6', 'e5', 'g5', 'Bg3', 'b5', 'Bb3', 'b4', 'Ne4', 'dxe5', 'Nxe5', 'a5', 'Ba4+', 'c6', 'Bxc6+', 'Nxc6', 'dxc6', 'Qxd1+', 'Rxd1', 'Bc8', 'Nd6+', 'exd6', 'Rxd6', 'Ne7', 'c7', 'Nd7', 'Bxd7', 'Rxd7', 'Rfe8', 'Bd6', 'Nf5+', 'Kd2', 'Bxb2', 'Re1', 'Bc3+', 'Kd1', 'Rxe1#'], ['e4', 'e5', 'Nf3', 'd6', 'd4', 'Bg4', 'h3', 'Bh5', 'g4', 'Bg6', 'dxe5', 'dxe5', 'Nxe5', 'Bxe4', 'f3', 'Qxd1+', 'Kxd1', 'Bd5', 'Bc4', 'c6', 'Nc3', 'Nf6', 'g5', 'Nfd7', 'Nxd5', 'cxd5', 'Bxd5', 'Na6', 'Bxb7', 'Rd8', 'Nxd7', 'Rxd7+', 'Ke2', 'Rxb7', 'Re1', 'Bb4', 'c3', 'Bc5', 'Kd3+', 'Re7', 'b4', 'Bb6', 'Be3', 'Nc7', 'Bxb6', 'axb6', 'a4', 'b5', 'c4', 'bxc4+', 'Kxc4', 'Kd7', 'b5', 'Rc8', 'Rad1+', 'Ke8', 'Rxe7+', 'Kxe7', 'Kb4', 'Ne6', 'a5', 'Nc7', 'b6', 'Na6+', 'Kb5', 'Nc5', 'Re1+', 'Kd6', 'f4', 'g6', 'h4', 'Nd7', 'Rd1+', 'Ke7', 'b7', 'Rb8', 'a6', 'Kd8', 'Kc6', 'Rc8+', 'bxc8=R+', 'Kxc8', 'Rxd7', 'Kb8', 'Rb7+', 'Ka8', 'a7', 'f5', 'Kb6', 'h5', 'Rb8#'], ['d4', 'Nc6', 'Nf3', 'd5', 'Bg5', 'Bf5', 'e3', 'e6', 'Bxd8', 'Nxd8', 'Bb5+', 'c6', 'Ba4', 'b5', 'Bb3', 'c5', 'Bxd5', 'exd5', 'Nc3', 'b4', 'Nxd5', 'Nc6', 'Nc7+', 'Kd7', 'Nxa8', 'cxd4', 'exd4', 'Nf6', 'd5', 'Nxd5', 'Qxd5+', 'Bd6', 'Qxf5+', 'Ke7', 'Rxa8', 'Rhe1+', 'Kd8', 'Rxd6+', 'Kc7', 'Qd7+', 'Kb6', 'Qxc6+', 'Ka5', 'Re5#'], ['e4', 'Nf6', 'e5', 'Ne4', 'Qf3', 'f5', 'd4', 'Ng5', 'Qxf5', 'Ne6', 'Qh5+', 'g6', 'Qg4', 'd6', 'Bc4', 'Ng7', 'Qe4', 'c5', 'Bd5', 'Qa5+', 'Nc3', 'e6', 'Bxb7', 'Bxb7', 'Qxb7', 'Qb6', 'Qxa8', 'Nf5', 'Bf4', 'Nxd4', 'exd6', 'Nxc2+', 'Kd2', 'Nxa1', 'd7+', 'Kxd7', 'Qxb8', 'Qxb8', 'Bxb8', 'Bd6', 'Bxa7', 'Rb8', 'Bxb8', 'Bxb8', 'a3', 'Bf4+', 'Kd3', 'c4+', 'Kxc4', 'Nc2', 'g3', 'Bd2', 'Nf3', 'Nxa3+', 'Kd3', 'Nc4', 'Nxd2', 'Nxb2+', 'Kc2', 'h5', 'h3', 'g5', 'h4', 'gxh4', 'gxh4', 'e5', 'Re1', 'Kd6', 'f3', 'Kc5'], ['Nf3', 'd5', 'd4', 'Nc6', 'e3', 'Bf5', 'c4', 'Nb4', 'Na3', 'dxc4', 'Bxc4', 'Nf6', 'Nc2', 'Nxc2+', 'Kf1', 'Nxa1', 'Bd3', 'e6', 'Bxf5', 'exf5', 'd5', 'Nxd5', 'Qxd5', 'Qxd5'], ['Nf3', 'd5', 'h3', 'Nc6', 'g4', 'e5', 'c3', 'Bc5', 'b4', 'Bb6', 'd3', 'Nf6', 'Be3', 'd4', 'Bd2', 'c4', 'e4', 'c5', 'exf3', 'e4', 'h5', 'Qxf3', 'hxg4', 'hxg4', 'Bxg4', 'Qg2', 'a5', 'cxb6', 'cxb6', 'b5', 'Ne5', 'f3', 'Nxf3+', 'Kf2', 'Nxd2', 'Nxd2', 'Qe7', 'Re1', 'Rac8', 'e5', 'Rc2', 'Kg1', 'Rxd2', 'Qxd2', 'Qxe5', 'Rxe5', 'Re8', 'Qh2', 'Bf3', 'Qh8#'], ['e4', 'e5', 'Nf3', 'Nc6', 'Bc4', 'd6', 'd4', 'exd4', 'Nxd4', 'Nxd4', 'Qxd4', 'Nf6', 'Nc3', 'c5', 'Qe3', 'Bd7', 'b5', 'Bd5', 'b4', 'Bxa8', 'Qxa8', 'Nd5', 'Nxd5', 'exd5+', 'Be7', 'Qe4', 'c3', 'Re8', 'cxb4', 'Bf6', 'Qc4', 'Be5', 'bxc5', 'dxc5', 'Qxc5', 'Rc8', 'Qe7', 'Re8', 'Qxd7', 'Qb8', 'Bg5', 'Bxh2+', 'Kh1', 'Rd8', 'Bxd8', 'Bc7', 'Bxc7'], ['e3', 'e5', 'Bd3', 'd5', 'Qh5', 'Nc6', 'Bb5', 'Nf6', 'Qxe5+', 'Be6', 'Nc3', 'a6', 'Bd3', 'Nxe5', 'Bxh7', 'Nxh7', 'Nxd5', 'Bxd5', 'e4', 'Bxe4', 'd3', 'Bxg2', 'Nf3', 'Bxh1', 'Nxe5', 'f6', 'Bg5', 'fxg5', 'Kd2', 'Bb4+', 'c3', 'Ba5', 'Re1', 'Rxh1', 'Rxf2+', 'Ke3', 'b5', 'Nc6', 'Qe8+', 'Kxf2', 'Qxc6', 'Re1', 'b4', 'c4', 'b3', 'Ra1', 'g4', 'axb3', 'Qf6+', 'Ke2', 'Qf3#'], ['b3', 'e5', 'Bb2', 'Nc6', 'Na3', 'd5', 'Nh3', 'Bc5', 'f4', 'Bxa3', 'Bxa3', 'Nf6', 'Bb2', 'd4', 'Ng5', 'Qd5', 'e4', 'Nxe4', 'd3', 'Nxg5', 'c4', 'Qa5+', 'Ke2', 'exf4', 'Qb1', 'Bg4+', 'Kf2', 'Qd2+', 'Be2', 'Bxe2', 'Bc3', 'dxc3'], ['e4', 'e5', 'Nf3', 'd6', 'Bc4', 'Bg4', 'Bxf3', 'Qxf3', 'Nf6', 'Nc3', 'c6', 'd3', 'b5', 'Bb3', 'Na6', 'Bg5', 'h6', 'Be3', 'g5', 'd4', 'Nb4', 'd5', 'cxd5', 'exd5', 'a5', 'Nxb5', 'a4', 'Bc4', 'Nxc2', 'Rac1', 'Nb4', 'a3', 'Nbxd5', 'Bxd5', 'Nxd5', 'Qxd5', 'Rb8', 'Nxd6+', 'Bxd6', 'Qc6+', 'Kf8', 'Bc5', 'Bxc5', 'Qxc5+', 'Kg7', 'Qxe5+', 'Kg8', 'Rcd1', 'Qc8', 'Rfe1', 'Qb7', 'Rd4', 'Qxb2', 'Rxa4', 'Qxe5', 'Rxe5', 'Kg7', 'g3', 'Rb1+', 'Kg2', 'f6', 'Re7+', 'Kg6', 'g4', 'Rd8', 'Raa7', 'f5', 'Rg7+', 'Kf6', 'Raf7+', 'Ke6', 'gxf5+', 'Ke5', 'Re7+', 'Kxf5', 'Rd7', 'Rf8', 'a4', 'Ke6', 'Rde7+', 'Kf6', 'Rb7', 'Ra1', 'Ra7', 'Ra2', 'a5', 'Ke6', 'Rge7+', 'Kd6', 'Red7+', 'Kc6', 'Rdc7+', 'Kb5', 'Rcb7+', 'Kc6', 'Rc7+', 'Kb5', 'Kg3', 'Ra3+', 'Kg4', 'Ra4+', 'Kh5', 'Rxf2', 'Kxh6', 'Rxh2+', 'Kxg5', 'Rg2+', 'Kf6', 'Rf2+', 'Ke7', 'Rd4', 'Rab7+', 'Kxa5', 'Rc5+', 'Ka6', 'Rb1', 'Re2+', 'Kf6', 'Rf4+', 'Kg5', 'Rf8', 'Rc6+', 'Ka7', 'Ra1+', 'Kb7', 'Rf6', 'Rg2+', 'Kf5', 'Rf2+', 'Ke6', 'R8xf6+', 'Ke7', 'R6f3', 'Rb1+', 'Kc6', 'Kd8', 'Rd2+', 'Kc8', 'Rc3', 'Kb8', 'Kc5', 'Kb7', 'Kc4', 'Kb6', 'Kd3', 'Kb5', 'Kc2', 'Rb4', 'Rd1', 'Ka4', 'Ra1+', 'Kb5', 'Rc8', 'Rd4', 'Rb1+', 'Ka6', 'Ra8#'], ['e4', 'd5', 'exd5', 'Qxd5', 'Nc3', 'Qd8', 'd4', 'Nf6', 'Bb5+', 'Bd7', 'Nf3', 'Bxb5', 'Nxb5', 'c6', 'Nc3', 'e6', 'Bd6', 'Be3', 'Qc7', 'Qd3', 'Ng4', 'Bg5', 'Nxh2', 'Kh1', 'Nxf1', 'Qxf1', 'h6', 'Bh4', 'g5', 'Bg3', 'Bxg3', 'fxg3', 'Nd7', 'Rd1', 'Qc4', 'Nb6', 'Qc5', 'Qxg3', 'd5', 'exd5', 'Qe7', 'Rhf8', 'Re1', 'g4', 'Ne2', 'Qd6', 'Ned4', 'Nc4', 'b3', 'Nb2', 'c3', 'Rde8', 'Qxe8+', 'Rxe8', 'Rxe8+', 'Kd7', 'Nf5', 'Kxe8', 'Nxd6+'], ['e4', 'e6', 'd4', 'd5', 'Nc3', 'Nf6', 'e5', 'Ne4', 'Qe2', 'Nxc3', 'bxc3', 'c5', 'Be3', 'c4', 'Nf3', 'Nc6', 'g3', 'Bd7', 'Bg2', 'Qc7', 'Bg5', 'Be7', 'a4', 'h6', 'Bxe7', 'Nxe7', 'a5', 'a6', 'g4', 'g6', 'g5', 'h5', 'h4', 'Rhe8', 'Rfb1', 'Nc6', 'Bh3', 'Kb8', 'Nd2', 'Ne7', 'f4', 'Ka8', 'Rb4', 'Rc8', 'Bg2', 'Bb5', 'Rf1', 'Qd7', 'Bxd5', 'Nxd5', 'Nxc4', 'Nxb4', 'Nb6+', 'Ka7', 'Nxc8+', 'Qxc8', 'Qe4', 'Bxf1', 'Kxf1', 'Qxc3', 'Qg2', 'Nxc2', 'Qf2', 'Nxd4', 'Kg2', 'Rc8', 'Kh2', 'Qc2', 'Kg3', 'Qxf2+', 'Kxf2', 'b5', 'axb6+', 'Kxb6', 'Ke3', 'Nb5', 'Ke4', 'a5', 'f5', 'Rc4+', 'Kd3', 'Rxh4', 'fxe6', 'fxe6', 'Ke3', 'Rd4', 'Kf3', 'a4', 'Ke3', 'a3', 'Ke2', 'a2', 'Ke3', 'a1=Q', 'Kf3', 'Qa3+', 'Kg2', 'Rd2+', 'Kf1', 'Qa1#'], ['d4', 'd5', 'Nf3', 'Nc6', 'c3', 'Nf6', 'Na3', 'e6', 'Nb5', 'Bd6', 'Nxd6+', 'Qxd6', 'Bg5', 'e5', 'dxe5', 'Nxe5', 'e4', 'dxe4', 'Qxd6', 'cxd6', 'Nd4', 'Bg4', 'f3', 'exf3', 'gxf3', 'Bxf3', 'Re1', 'Bxh1', 'Bb5', 'a6', 'Ba4', 'Nd3+'], ['d4', 'd5', 'b3', 'Nc6', 'a3', 'e5', 'e3', 'Nf6', 'Ne2', 'g6', 'dxe5', 'Nxe5', 'f3', 'Bg7', 'Nd4', 'b6', 'Nb5', 'Bb7', 'Bb2', 'Qd7', 'Bxe5', 'Bxf6', 'Bxf6', 'c3', 'c6', 'Nd4', 'c5', 'Nb5', 'a6', 'c4', 'axb5', 'cxb5', 'd4', 'exd4', 'cxd4', 'Ra2', 'Rfe8+', 'Be2', 'Bh4+', 'g3', 'Bg5', 'Red8', 'Bd3', 'f5', 'a4', 'Be4', 'fxe4', 'fxe4', 'Bxe4', 'd3', 'Bxa8', 'Rxa8', 'Rd2', 'Bxd2', 'Qxd2', 'Rd8', 'Rd1', 'Qd4+', 'Qf2', 'Qxf2+', 'Kxf2', 'Rf8+', 'Ke3', 'Rd8', 'Rxd3', 'Rxd3+', 'Kxd3', 'h5', 'Nc3', 'Kf7', 'Nd5', 'Ke6', 'Nxb6', 'Kf5', 'h3', 'g5', 'Nd5', 'g4', 'Ne3+', 'Kg5', 'hxg4', 'h4', 'gxh4+', 'Kxh4'], ['e4', 'e5', 'Nf3', 'Nc6', 'Nc3', 'Bc5', 'Bc4', 'Nf6', 'd3', 'Be3', 'd6', 'Bxe3', 'fxe3', 'Be6', 'd4', 'd5', 'dxe5', 'dxc4', 'exf6', 'Qxd1', 'Raxd1', 'Rad8', 'fxg7', 'Rfe8', 'Nb5', 'Rxd1', 'Rxd1', 'Rd8', 'Rxd8+', 'Nxd8', 'Nxc7', 'a5', 'Ne5', 'c3', 'bxc3', 'Bxa2', 'Nd5', 'a4', 'Ne7+', 'Kxg7', 'Nf5+', 'Kf6', 'Ng4+', 'Kg5', 'h3', 'Be6', 'c4', 'a3', 'Nd4', 'Bxc4', 'Nf3+', 'Kh5', 'Nf6+', 'Kg6', 'Ne5+', 'Kxf6', 'Nxc4', 'a2', 'e5+', 'Ke6', 'Nd2', 'a1=Q+', 'Nf1', 'Nc6', 'Kf2', 'Nxe5', 'Ng3', 'f5', 'h4', 'Qa2', 'Kg1', 'Qxc2', 'Kh2', 'b5'], ['e4', 'f5', 'exf5', 'e6', 'fxe6', 'Bc5', 'd4', 'Bb6', 'exd7+', 'Bxd7', 'Nf3', 'c5', 'Bc4', 'cxd4', 'Nxd4', 'Nf6', 'Nc3', 'Bg4', 'f3', 'Bxd4', 'fxg4', 'Bxc3+', 'bxc3', 'Qxd1+', 'Kxd1', 'Ne4', 'Bb5+', 'Nd7', 'Re1', 'Bd3', 'Nxc3+', 'Kd2', 'Rac8', 'Re7', 'h6', 'Rxd7', 'Rf2+', 'Ke3', 'Rxg2', 'Rxb7', 'Ne2', 'Bxe2', 'Rxc2', 'Rxa7', 'Rc3+', 'Kd2', 'Rh3', 'Rb1', 'Rhxh2', 'Ke3', 'Rxe2+', 'Kf3', 'Rhf2+', 'Kg3', 'Rg2+', 'Kf3', 'Rgf2+', 'Kg3', 'Rg2+', 'Kh4', 'Ref2', 'g5', 'Rh2+', 'Kg4', 'Rhg2+', 'Kh5', 'Rf3', 'Rb8+', 'Kh7', 'g6+', 'Rxg6', 'Raa8', 'Rh3#'], ['d4', 'd5', 'c4', '{[%clk']]


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
        else:
            print("This was not a better move.")

        print("The best move was " + bestmove)
    except:
        print("Not a valid move.")

    print("Would you like to do another one? (y or n)")
    answer = input()
