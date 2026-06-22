class Settings:
    """Class for saving all settings for the game"""

    def __init__(self):
        """Initialized game settings"""
        self.screen_width = 1_200
        self.screen_height = 800

        # Window background color
        self.bg_color = (20, 30, 55)

        # Ship Settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullet_allowed = 6

        # Alien Settings
        self.fleet_drop_speed = 10

        # Increase speed temp of the game
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialized settings that change during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction = 1 define moving to the right; -1 - to the left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale