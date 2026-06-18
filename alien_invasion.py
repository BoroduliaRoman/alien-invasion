import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class for manage resources and game behavior"""

    def __init__(self):
        """Initialized game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Launch main game loop"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Tracking events keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # For each loop cycle redrawn screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        """Display last screen"""
        pygame.display.flip()


if __name__ == '__main__':
    """Create an example and launch game"""
    ai = AlienInvasion()
    ai.run_game()