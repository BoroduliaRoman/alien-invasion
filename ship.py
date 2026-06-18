import pygame

class Ship:
    """Class for the ship control"""

    def __init__(self, ai_game):
        """Initialized and target start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rectangle
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (64, 54))
        self.rect = self.image.get_rect()
        # Every new ship appear in the screen bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)