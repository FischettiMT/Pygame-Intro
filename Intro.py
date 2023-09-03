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
            
    pygame.draw.circle(screen,"yellow",(screen_width/2,screen_height/2), 100, 0)
    pygame.draw.circle(screen,"red",(screen_width/4,screen_height/4), 50, 0)
    
    
    
    
    pygame.display.flip()

    





