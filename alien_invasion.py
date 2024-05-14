import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
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
        gf.check_events(ship)
        
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, ship)
        
        
run_game()
         
        
    
