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
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import config, utils
from font import Font 
from components.common import Drawable
from views import game

class LatinSquares:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

        self.gameDisplay = None
        self.info = None
        self.update_function = None
        self.bg = (0, 0, 0)
        self.prev_update_function = None

    def vw(self, x):
        return (x / 100) * self.display_rect.width

    def vh(self, y):
        return (y / 100) * self.display_rect.height

    def blit_centred(self, surf, x, y):
        rect = surf.get_rect()
        centered_coords = (x - rect.width // 2, y - rect.height // 2)
        self.gameDisplay.blit(surf, centered_coords)

    def stop(self):
        self.running = False

    def set_screen(self, view):
        view(self)

    def set_background(self, color):
        self.bg = color

    def show_help(self):
        if self.prev_update_function is None:
            self.prev_update_function = self.update_function
            self.update_function = self.help_popup.update
        else:
            self.update_function = self.prev_update_function


    def run(self):
        self.gameDisplay = pygame.display.get_surface()
        self.info = pygame.display.Info()
        self.display_rect = self.gameDisplay.get_rect()

        config.load_images()
        config.font.intialize("./assets/fonts/Geist.ttf")

        self.bg = config.background_color
        self.set_screen(game.view)

        self.help_image = config.images["misc"]["help"]
        self.help_image = utils.scale_image_maintain_ratio(self.help_image, h=self.vh(100))

        self.help_popup = Drawable()
        self.help_popup.gameDisplay = self.gameDisplay
        self.help_popup.x = self.vw(3)
        self.help_popup.y = self.vh(0)
        self.help_popup.set_image_rect(self.help_image)

        if not (self.gameDisplay):
            self.gameDisplay = pygame.display.set_mode(
                (self.info.current_w, self.info.current_h))
            pygame.display.set_caption("Latin Squares Activity")

        while self.running:
            self.gameDisplay.fill(self.bg)

            if self.update_function is not None:
                self.update_function()

            while Gtk.events_pending():
                Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            pygame.display.update()
            self.clock.tick(60)

        return


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = LatinSquares()
    game.run()
