#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "cbarange"
__date__ = "22th October 2020"
"""
--- TODO ---
use State Machine
check for https://github.com/xamox/pygame/blob/master/examples/aliens.py

--- Setup dependencies ---
pip3 freeze > requirements.txt
pip3 install -r requirements.txt

--- Start Virtual Environment ---
sudo apt install -y python3-venv
pip3 install --user virtualenv
python3 -m venv `pwd`
source `pwd`/bin/activate
deactivate

--- Run Script ---
chmod +x `pwd`/src/main.py
`pwd`/src/main.py

--- Compile Script as Binary ---


"""
import pygame
import requests
from pygame.locals import *
import util
import global_store as store
import display

def init_main_window():
	# --- Initialisation de pygame ---
	pygame.init()
	store.screen = pygame.display.set_mode(store.windows_size)
	# Set Icone
	pygame.display.set_icon(pygame.image.load(util.get_asset_path(store.icone_image)).convert_alpha())
	# Set title
	pygame.display.set_caption(store.windows_title)

def init_game():
	store.current_display = display.Display()

def main():
	init_main_window()
	init_game()
	clock = pygame.time.Clock()
	while not store.is_main_window_closed:
		# - Rafraichissement -
		store.screen.fill((0,0,0,0))
		# - Display -		
		store.current_display.draw()
		pygame.display.flip()

		clock.tick(store.fps_max) # default is 60 FPS

if __name__ == "__main__":
	main()

else:
	print(f"Error: {__name__} must be run as script")



