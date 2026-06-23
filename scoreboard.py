import pygame.font

class Scoreboard:
    """Class for showing game info"""

    def __init__(self, ai_game):
        """Initialized attributes score counting"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for showing score
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(name=None, size=48)

        # Preparing image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Transform current score to graph image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Show score in upper right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Show score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_high_score(self):
        """Transform high record score in graph image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Place record in top center screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Checked if exist new high record"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Transform level score in graph image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # Level shows under current score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10