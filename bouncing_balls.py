import pygame
import os
import random
import bouncing_balls_class

# clear terminal
os.system('cls')

# screen size 
screen_width = 1900
screen_height = 1000
screen_size = (screen_width, screen_height)

# pygame initialization
pygame.init()

# create pygame screen
win = pygame.display.set_mode(screen_size)

# create clock
fps_clock = pygame.time.Clock()
fps = 60

num_of_balls = 1000

# def __init__(self,radius,x_init,y_init,x_speed,y_speed,clr,screen):
balls = []

for ball in range(num_of_balls):
    balls.append(bouncing_balls_class.Ball(
        random.randint(25,100),
        random.randint(0,screen_width),
        random.randint(0,screen_height),
        random.randint(8,12),
        random.randint(8,12),
        -1,win))
    

# start game loop
run = True
while run == True:
    win.fill("yellow")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            run = False
            
    for ball in balls:
        ball.update()
        ball.draw()
   
    pygame.display.flip()
# end game loop

pygame.quit()  