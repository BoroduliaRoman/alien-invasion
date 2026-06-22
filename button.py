import pygame.font

class Button:
    """Initialized button attributes"""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Define sizes and button properties
        self.width, self.height = 200, 50
        self.button_color = (0, 77, 64)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build object rect button and placed by screen center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message creates only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transform msg in rectangle and placed by center"""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Display empty button and show message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)