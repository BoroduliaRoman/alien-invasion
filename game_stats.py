class GameStats:
    """Tracking statistic for the Alien Invasion Game"""

    def __init__(self, ai_game):
        """Initialized statistic"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game Alien Invasion launch in active state
        self.game_active = False

    def reset_stats(self):
        """Initialized statistic that changing during the game"""
        self.ships_left = self.settings.ship_limit