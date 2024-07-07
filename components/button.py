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
                 font=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        self.img = pygame.Surface((w, h))
        self.rect = pygame.Rect((0, 0), (w, h))
        self.color = config.accent_color

        pygame.draw.rect(self.img, self.color, self.rect)

        if font is None:
            font = config.font.lg

        # Generate and blit the Label on button
        text_color = config.front_color
        label = font.render(label, True, text_color)
        label_rect = label.get_rect()
        label_rect.x = self.rect.width // 2 - label_rect.width // 2
        label_rect.y = self.rect.height // 2 - label_rect.height // 2
        self.img.blit(label, label_rect)

        self.set_image_rect(self.img,
                            x,
                            y)

    def update(self):
        Clickable.update(self)
        Drawable.update(self)
