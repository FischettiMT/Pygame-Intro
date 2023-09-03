import pygame
import os

# clear terminal
os.system("cls")

# screen size
screen_width = 1024
screen_height = 768
screen_size = (screen_width, screen_height)

# pygame initialization
pygame.init()

# create squ
squ = pygame.Rect((10, 10, 30, 30))
squ_speed_x = 6
squ_speed_y = 6

# create rect
rec = pygame.Rect((100, 10, 130, 50))
rec_speed_x = 6
rec_speed_y = 6

# create pygame screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Moving a SQUARE with arrow keys - By Max Fischetti")

# create clock
fps_clock = pygame.time.Clock()
fps = 60

screen.fill("cyan")
run = True
# start game loop
while run == True:
    fps_clock.tick(fps)
    screen.fill("cyan")

    pygame.draw.rect(screen, "red", squ)
    pygame.draw.rect(screen, "green", rec)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
          
    squ.x += squ_speed_x
    squ.y += squ_speed_y
    
    if squ.right >= screen_width:
        squ_speed_x *= -1
    if squ.bottom >= screen_height:
        squ_speed_y *= -1
    if squ.left <= 0:
        squ_speed_x *= -1
    if squ.top <= 0:
        squ_speed_y *= -1
        
          
    rec.x += rec_speed_x
    rec.y += rec_speed_y
    
    if rec.right >= screen_width:
        rec_speed_x *= -1
    if rec.bottom >= screen_height:
        rec_speed_y *= -1
    if rec.left <= 0:
        rec_speed_x *= -1
    if rec.top <= 0:
        rec_speed_y *= -1

    pygame.display.flip()
# end of game loop

print("game over")
