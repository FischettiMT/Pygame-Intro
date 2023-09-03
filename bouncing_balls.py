import pygame
import os
import bouncing_balls_class

# clear terminal
os.system('cls')

# screen size 
screen_width = 1_024
screen_height = 768
screen_size = (screen_width, screen_height)

# pygame initialization
pygame.init()

# create pygame screen
win = pygame.display.set_mode(screen_size)

# create clock
fps_clock = pygame.time.Clock()
fps = 60

num_of_balls = 10

ball1 = bouncing_balls_class.Ball(50,512,384,2,1,-1,win)
ball2 = bouncing_balls_class.Ball(25,512,384,1,2,"cyan",win)
ball3 = bouncing_balls_class.Ball(50,256,192,2,1,-1,win)
ball4 = bouncing_balls_class.Ball(25,375,400,1,2,-1,win)


# start game loop
run = True
while run == True:
    fps_clock.tick(fps) 
    win.fill("red")-
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    ball1.update()
    ball1.draw()
    
    ball2.update()
    ball2.draw()
            
    ball3.update()
    ball3.draw()
    
    ball4.update()
    ball4.draw()
   
    
    
    
    pygame.display.flip()
# end game loop

pygame.quit()  