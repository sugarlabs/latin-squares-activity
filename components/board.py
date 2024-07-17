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
        self.ops_matrix_hor = []
        self.ops_matrix_ver = []
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.on_win = None

        self.buttons = []
        self.answers = []

        self.to_be_checked = []
        self.rot_buttons = []

    def generate_game(self, size, missing):
        # Generate random numbers and operators for the game board
        for _ in range(size):
            nums = [math.floor(random() * size) + 1 for __ in range(size)]
            self.nums_matrix.append(nums)
        
        for _ in range(size):
            ops = [choice(["+", "-", "*"]) for __ in range(size - 1)]
            self.ops_matrix_ver.append(ops)
        
        for _ in range(size - 1):
            ops = [choice(["+", "-", "*"]) for __ in range(size)]
            self.ops_matrix_hor.append(ops)

        missed = 0

        # Create button objects for each number and operator
        box_size = self.w // (len(self.nums_matrix) * 2 - 1)
        for i, nums in enumerate(self.nums_matrix):
            y = box_size * 2 * i
            for j, num in enumerate(nums):
                if missed < missing and random() < 1 / (2 * size - missing):
                    missed += 1
                    n = math.floor(random() * (size + 1)) + 1
                    rot_btn = (Button(self.x + 2 * j * box_size, y, f"{n}", w=box_size, h=box_size, font=config.font.xl, image=config.images["tiles"]["green"], text_color=(255, 0, 0)))
                    rot_btn.rotatable(size)
                    self.buttons.append(rot_btn)
                    self.to_be_checked.append(num)
                    self.rot_buttons.append(rot_btn)
                else:
                    self.buttons.append(Button(self.x + 2 * j * box_size, y, f"{num}", w=box_size, h=box_size, font=config.font.xl, image=config.images["tiles"]["blue"]))
        
        for i, ops in enumerate(self.ops_matrix_ver):
            y = box_size * (2 * i)
            for j, op in enumerate(ops):
                self.buttons.append(Button(self.x + (2 * j + 1) * box_size, y, f"{op}", w=box_size, h=box_size, font=config.font.xxl))
        
        for i, ops in enumerate(self.ops_matrix_hor):
            y = box_size * (2 * i + 1)
            for j, op in enumerate(ops):
                self.buttons.append(Button(self.x + (2 * j) * box_size, y, f"{op}", w=box_size, h=box_size, font=config.font.xxl))
        
        self.calculate_and_create_answers(box_size)

    def calculate_and_create_answers(self, box_size):
        # Calculate and create buttons for the answers of each row
        for i, nums in enumerate(self.nums_matrix):
            result = nums[0]
            for j, op in enumerate(self.ops_matrix_ver[i]):
                if op == '+':
                    result += nums[j + 1]
                elif op == '-':
                    result -= nums[j + 1]
                elif op == '*':
                    result *= nums[j + 1]
                elif op == '/':
                    result /= nums[j + 1]
            y = box_size * 2 * i
            self.answers.append(Button(self.x + (len(nums) * 2 - 1) * box_size + 16, y, f"{result}", w=box_size, h=box_size, font=config.font.xl))

        # Calculate and create buttons for the answers of each column
        for j in range(len(self.nums_matrix[0])):
            result = self.nums_matrix[0][j]
            for i in range(len(self.ops_matrix_hor)):
                op = self.ops_matrix_hor[i][j]
                if op == '+':
                    result += self.nums_matrix[i + 1][j]
                elif op == '-':
                    result -= self.nums_matrix[i + 1][j]
                elif op == '*':
                    result *= self.nums_matrix[i + 1][j]
                elif op == '/':
                    result /= self.nums_matrix[i + 1][j]
            x = box_size * 2 * j
            self.answers.append(Button(self.x + x, (len(self.nums_matrix) * 2 - 1) * box_size + 16, f"{result}", w=box_size, h=box_size, font=config.font.xl))

    def game_over_check(self):
        for i in range(len(self.rot_buttons)):
            if str(self.rot_buttons[i].label) != str(self.to_be_checked[i]):
                return False
        if self.on_win is not None:
            self.on_win()
        return True
        
    
    def draw(self):
        # Draw the game board and answer buttons
        for btn in self.buttons + self.answers:
            btn.draw()

    def update(self):
        # Update the state of all buttons
        self.game_over_check()
        for btn in self.buttons + self.answers:
            btn.update()
