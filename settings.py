class Settings:
    """Class for saving all settings for the game"""

    def __init__(self):
        """Initialized game settings"""
        self.screen_width = 1_200
        self.screen_height = 800

        # Window background color
        self.bg_color = (20, 30, 55)

        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullet_allowed = 6

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1