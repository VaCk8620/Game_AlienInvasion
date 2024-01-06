import pygame

class Ship():
    def __init__(self,screen):
        """Initialize the ship and sets starting position(x,y)"""
        self.screen = screen
        
        #Load ship image and rect.
        self.image       = pygame.image.load('main_project\images\_player_spaceship.bmp')
        self.rect        = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        
        #Movement Flags
        self.moving_right = False
        
    def update(self):
        """Update ship's position based on movement flag"""
        if self.moving_right:
            self.rect.centerx += 1
        

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image,self.rect)