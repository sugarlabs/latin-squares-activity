# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import config
import utils
import pygame
from random import random, choice
import math

class Board():
    def __init__(self, x, y, w, h):
        super().__init__()
        self.gameDisplay = pygame.display.get_surface()

        self.nums_matrix = []
        self.ops_matrix = []
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def generate_game(self, size):
        for _ in range(size):
            nums = []
            for __ in range(size):
                nums.append(math.floor(random() * (size + 1)) + 1)
            self.nums_matrix.append(nums)
        for _ in range(size):
            ops = []
            for __ in range(size - 1):
                ops.append(choice(["+", "-", "/", "*"]))
            self.ops_matrix.append(ops)

        print(self.ops_matrix)
        print(self.nums_matrix)

    def game_over_check(self, turn):
            over = True
            for row in self.game_matrix:
                if len(row) != 0:
                     over = False
            if not over:
                 return False
            
            if turn == 0:
                 self.end_game("win")
            if turn == 1:
                 self.end_game("lose")
            return True

    def update(self):
        for row in self.game_matrix:
            for o in row:
                o.update()
