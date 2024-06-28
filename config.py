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


import os
import pygame
from font import Font


font = Font()
background_color = (245, 225, 231)
front_color = (0, 0, 0)                                                    

images = {}

def load_images():
    for dir in ["tiles"]:
        dir_images = {}
        directory = f"assets/images/{dir}"
        for filename in os.listdir(directory):
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                file_path = os.path.join(directory, filename)
                try:
                    image = pygame.image.load(file_path)
                    base_filename = os.path.splitext(filename)[0]
                    dir_images[base_filename] = image
                except pygame.error as err:
                    print(f"Error loading image '{file_path}': {err}")
        images[dir] = dir_images
