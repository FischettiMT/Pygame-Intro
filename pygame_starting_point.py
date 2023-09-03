import pygame
import os

# clear terminal
os.system('cls')

# screen size 
screen_width = 1_024
screen_height = 768
screen_size = (screen_width, screen_height)

# pygame initialization
pygame.init()

# create pygame screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Moving a SQUARE with arrow keys - By Max Fischetti")


# create clock
fps_clock = pygame.time.Clock()
fps = 60

# start game loop
run = True
while run == True:
    fps_clock.tick(fps) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
    
    
    
    pygame.display.flip()
