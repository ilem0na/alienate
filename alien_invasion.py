import sys
import pygame
from settings import Settings
from ship import Ship
from game_functions import check_events
def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    
    # start main loop for game 
    while True:
        
        # watch for keyboard and mouse events.
        check_events()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
run_game()
         
        
    
