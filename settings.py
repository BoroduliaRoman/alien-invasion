class Settings:
    """Class for saving all settings for the game"""

    def __init__(self):
        """Initialized game settings"""
        self.screen_width = 1_200
        self.screen_heigh = 800

        # Window background color
        self.bg_color = (230, 230, 230,)