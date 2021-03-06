import numpy as np
from math import *

class Game:
    def __init__(self):
        self.board = []
        self.player = 1
        self.moves = []
        self.time_mode = "none"
        self.time_limit = 5

        for x in range(4):
            t = []
            for y in range(4):
                t.append([0,0,0,0])
            self.board.append(t)

    def set_time_mode(self,mode):
        self.time_mode = mode

    def set_time_limit(self,lim):
        self.time_limit = lim

    def print_board(self):
        for x in self.board:
            print(np.array(x))
            print()


    def allowed_moves(self):
        n = 1
        allowed = []
        for x in range(4):
            for y in range(4):
                if self.board[3][y][x] == 0:
                    allowed.append(x*4+y+1)
                n+=1
        return allowed

    def move(self,place):
        if place in self.allowed_moves():
            self.moves.append(place)
            x = 0
            while 1:
                if self.board[x][(place-1)%4][floor((place-1)/4)] == 0:
                    self.board[x][(place-1) % 4][floor((place-1) / 4)] = self.player
                    if self.player == 1:
                        self.player = -1
                    else:
                        self.player = 1
                    break
                else:
                    x+=1

    def check_board(self):
        for layer in self.board:
            for row in layer:
                if len([1 for x in row if x == 1]) == 4:
                    return 1
                if len([1 for x in row if x == -1]) == 4:
                    return -1
            for coll in range(4):
                if len([1 for x in range(4) if layer[x][coll] == 1]) == 4:
                    return 1
                if len([1 for x in range(4) if layer[x][coll] == -1]) == 4:
                    return -1
            if len([1 for x in range(4) if layer[x][x] == 1]) == 4:
                return 1
            if len([1 for x in range(4) if layer[x][x] == -1]) == 4:
                return -1
            if len([1 for x in range(4) if layer[x][3-x] == 1]) == 4:
                return 1
            if len([1 for x in range(4) if layer[x][3-x] == -1]) == 4:
                return -1

        for row in range(4):
            for coll in range(4):
                if len([1 for layer in range(4) if self.board[layer][row][coll] == 1]) == 4:
                    return 1
                if len([1 for layer in range(4) if self.board[layer][row][coll] == -1]) == 4:
                    return -1
            if len([1 for x in range(4) if self.board[x][row][x] == 1]) == 4:
                return 1
            if len([1 for x in range(4) if self.board[x][row][x] == -1]) == 4:
                return -1
            if len([1 for x in range(4) if self.board[x][row][3-x] == 1]) == 4:
                return 1
            if len([1 for x in range(4) if self.board[x][row][3-x] == -1]) == 4:
                return -1

            if len([1 for x in range(4) if self.board[x][x][row] == 1]) == 4:
                return 1
            if len([1 for x in range(4) if self.board[x][x][row] == -1]) == 4:
                return -1
            if len([1 for x in range(4) if self.board[x][3-x][row] == 1]) == 4:
                return 1
            if len([1 for x in range(4) if self.board[x][3-x][row] == -1]) == 4:
                return -1
        if len([1 for x in range(4) if self.board[x][x][x] == 1]) == 4:
            return 1
        if len([1 for x in range(4) if self.board[x][x][x] == -1]) == 4:
            return -1
        if len([1 for x in range(4) if self.board[x][x][3-x] == 1]) == 4:
            return 1
        if len([1 for x in range(4) if self.board[x][x][3-x] == -1]) == 4:
            return -1
        if len([1 for x in range(4) if self.board[x][3-x][x] == 1]) == 4:
            return 1
        if len([1 for x in range(4) if self.board[x][3-x][x] == -1]) == 4:
            return -1
        if len([1 for x in range(4) if self.board[x][3 - x][3 - x] == 1]) == 4:
            return 1
        if len([1 for x in range(4) if self.board[x][3 - x][3 - x] == -1]) == 4:
            return -1
        if not self.allowed_moves():
            return "tie"

    def undo_move(self):
        x = 3
        while 1:
            if self.board[x][(self.moves[-1]-1)%4][floor((self.moves[-1]-1)/4)] != 0:
                self.board[x][(self.moves[-1]-1) % 4][floor((self.moves[-1]-1) / 4)] = 0
                if self.player == 1:
                    self.player = -1
                else:
                    self.player = 1
                break
            else:
                x-=1
        self.moves.pop()
