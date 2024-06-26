import sys
import pygame
from settings import Settings
from ship import Ship

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move the ship to the right 
                    ship.moving_right = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                     # move the ship to the left
                        ship.moving_left = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        ship.moving_left = False
                    
           
                
def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    
    # redraw the screen through each iter of the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
    