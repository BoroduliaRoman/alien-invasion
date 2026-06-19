import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for control bullets that launch from the ship"""

    def __init__(self, ai_game):
        """Create bullet object in the current ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet in position (0,0) and setup correct position
        self.rect = pygame.Rect(
            0,0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position in float format
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up to screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)