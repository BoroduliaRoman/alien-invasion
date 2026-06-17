import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Class for manage resources and game behavior"""

    def __init__(self):
        """Initialized game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_heigh)
        )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Launch main game loop"""
        while True:
            """Tracking events keyboard and mouse"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # For each loop cycle redrawn screen
            self.screen.fill(self.settings.bg_color)

            """Display last screen"""
            pygame.display.flip()


if __name__ == '__main__':
    """Create an example and launch game"""
    ai = AlienInvasion()
    ai.run_game()