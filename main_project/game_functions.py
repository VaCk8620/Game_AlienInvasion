import sys
import pygame

def check_events(ship):
    """Responds to mouse and keypresss"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        
        elif event.type  == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(ai_settings, screen,ship):
    """Update images on the screen and flip to the new screen"""
    
    #Redraw the screen for each pass in the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #Make the most recently drawn screen visible
    pygame.display.flip()
    


    
    
    

    