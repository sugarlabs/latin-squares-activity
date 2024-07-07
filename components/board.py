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
from components.button import Button

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

        self.buttons = []

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

        box_size = self.w // (len(self.nums_matrix) + len(self.ops_matrix))
        for i, nums in enumerate(self.nums_matrix):
            y = box_size * 2 * i
            for j, num in enumerate(nums):
                 self.buttons.append(Button(self.w + 2 * j * box_size, y, f"{num}", w = box_size, h = box_size, font=config.font.xl))
            for i, ops in enumerate(self.ops_matrix):
                y = box_size * (2 * i)
                for j, op in enumerate(ops):
                    self.buttons.append(Button(self.w + (2 * j + 1) * box_size, y, f"{op}", w = box_size, h = box_size, color = config.background_color, font=config.font.xxl))

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
    
    def draw(self):
         pass

    def update(self):
        for btn in self.buttons:
             btn.update()
