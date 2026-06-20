import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class represent one alien"""

    def __init__(self, ai_game):
        """Initialized alien and set up his starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Download image and set up rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (96, 81))
        self.rect = self.image.get_rect()

        # Every new alien appear in upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saved accurate horizontal alien position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returned True if the alien locate in the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien ship to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x