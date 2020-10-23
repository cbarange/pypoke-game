# -*- coding: utf-8 -*-
import pygame
import util
import global_store as store


class Display():
	def __init__(self):
		self.current_display = WelcomDisplay()

	def draw(self):
		store.screen.blit(self.current_display.background, (0,0))
		"""
		# - Ajout de tous les elements de l'ecran -
		for item in currentDisplay.decorList:
			screen.blit(item.surf, item.position)
		screen.blit(currentDisplay.perso.surf, currentDisplay.perso.position)
		"""

class WelcomDisplay():
	
	def __init__(self):
		self.background = pygame.image.load(util.get_asset_path(store.main_background)).convert()
		self.background = pygame.transform.scale(self.background, store.windows_size)





