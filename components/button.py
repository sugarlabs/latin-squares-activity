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


import pygame
import config
import utils
from components.common import Clickable, Drawable


class Button(Clickable, Drawable):
    def __init__(self, x, y,
                 label, w=None, h=None,
                 font=None, text_color=None, image=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()
        
        self.x = x
        self.modulo = 0
        self.rotatablity = False
        self.y = y
        self.label = label
        self.w = w
        self.h = h
        self.font =font
        self.text_color = text_color
        self.img = image
        self.initialize()


    def initialize(self):
        if self.img is None:
            self.img = config.images["tiles"]["none"]
        self.image = self.img
        if self.w is not None:
            self.image = utils.scale_image_maintain_ratio(self.image, w=self.w)
        if self.h is not None:
            self.image = utils.scale_image_maintain_ratio(self.image, h=self.h)

        self.rect = pygame.Rect((0, 0), (self.w, self.h))

        # pygame.draw.rect(self.image, self.color, self.rect)

        if self.font is None:
            self.font = config.font.lg

        # Generate and blit the Label on button
        if self.text_color is None:
            self.text_color = config.front_color
        label = self.font.render(self.label, True, self.text_color)
        label_rect = label.get_rect()
        label_rect.x = self.rect.width // 2 - label_rect.width // 2
        label_rect.y = self.rect.height // 2 - label_rect.height // 2
        self.image.blit(label, label_rect)

        self.set_image_rect(self.image,
                            self.x,
                            self.y)
        
    def rotatable(self, modulo):
        self.modulo = modulo
        self.rotatablity = True
        self.on_click = self.rotate

    def rotate(self):
        if self.rotatablity == True:
            self.label = f"{((int(self.label) + 1) % (self.modulo + 1))}"
            self.initialize()

    def update(self):
        Clickable.update(self)
        Drawable.update(self)
