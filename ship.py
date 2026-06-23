import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Class for the ship control"""

    def __init__(self, ai_game):
        """Initialized and target start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rectangle
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (64, 54))
        self.rect = self.image.get_rect()

        # Every new ship appear in the screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Saving float center coordinate of the ship
        self.x = float(self.rect.x)

        # Moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position according to flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update attribute rect on self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Locate ship in the middle bottom screen part"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)