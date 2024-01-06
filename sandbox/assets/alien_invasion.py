'''Imports'''
import sys
import pygame

def run_game():
    #Initialize and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    #Main loop for game
    while True:
        
        #Catch keyboard strokes and mouse
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                sys.exit()
                
        #Make the most recently drawn screen visible
        pygame.display.flip()
        
run_game()