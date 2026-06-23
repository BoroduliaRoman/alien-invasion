import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Class for manage resources and game behavior"""

    def __init__(self):
        """Initialized game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Create instance for saving game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Create button Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Launch main game loop"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Tracking events keyboard and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event=event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event=event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_key_down_events(self, event):
        """React to press the button"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def check_keyup_events(self, event):
        """React to unpress the button"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and include it to Bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        # Delete bullets that gone out of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collusion()

    def _check_bullet_alien_collusion(self):
        """Processing collusion between bullets and aliens"""
        # Delete bullets and aliens in collusion
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # Check hit in aliens
        # When found hit - del bullet and alien
        if not self.aliens:
            # Delete exist bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """Create invasion fleet"""
        # Create alien and calculation amount of aliens in the row
        # Interval between aliens equal to width one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Define amount of rows, placing on the screen"""
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # Create first row of the aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # Create alien and placement hin in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update position all aliens in a fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Check collisions alien - ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if the aliens get bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """React to catch edges of the screen by aliens"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_float_direction()
                break

    def _change_float_direction(self):
        """Degree all fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        # For each loop cycle redrawn screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Show score info
        self.sb.show_score()

        # Button Play display only if game not active
        if not self.stats.game_active:
            self.play_button.draw_button()

        """Display last screen"""
        pygame.display.flip()

    def _ship_hit(self):
        """Processing hits between ship and alien"""
        if self.stats.ships_left > 0:
            # Decrease ships_left
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Clearing lists aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and move ship to the middle
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Checked if the aliens got the screen bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Do the same as hit between alien and ship
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """Launch new game when mouse click on the button 'Play'"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Clen aliens and bullets lists
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and move ship to center
            self._create_fleet()
            self.ship.center_ship()

            # Hover mouse pointer
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    """Create an example and launch game"""
    ai = AlienInvasion()
    ai.run_game()