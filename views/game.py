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
import math
import time
from components.board import Board
from components.common import Drawable
from levels import LEVELS

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    level = {"current" : 0, "label" : Drawable(), "timer" : 0, "timer_label" : Drawable(), "times" : []}
    level["label"].gameDisplay = game.gameDisplay
    level["timer_label"].gameDisplay = game.gameDisplay

    board_size = vh(75)
    board = Board((vw(100) - board_size) // 2,((vh(100) - board_size) // 2) - 32, board_size, board_size)

    def next_level():
        if level["current"] > 0:
            level["times"].append(level["timer"])
            level["timer"] = 0

        level["current"] += 1
        lvl = level["current"]
        board.generate_game(LEVELS[lvl][0], LEVELS[lvl][1])
        
        level_label = config.font.xxl.render(f"Level {lvl}", True, config.front_color)
        level["label"].set_image_rect(level_label, vw(5), vh(3))


    next_level()
    board.on_win = next_level


    def update():
        board.update()
        level["label"].update()
        level["timer_label"].update()

        level["timer"] = level["timer"] + 1
        timer = time.strftime('%M:%S', time.gmtime(level["timer"] / 60))
        timer_label = config.font.xl.render(f"{timer}", True, config.front_color)
        level["timer_label"].set_image_rect(timer_label, vw(5), vh(10))


    game.update_function = update
