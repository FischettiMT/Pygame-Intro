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

# create player
player = pygame.Rect((0, 0, 30, 60))
player_speed = 1

# create pygame screen
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Moving a SQUARE with arrow keys - By Max Fischetti")

# create clock
fps_clock = pygame.time.Clock()
fps = 120

# start game loop
run = True
while run == True:
    fps_clock.tick(fps)
    screen.fill("cyan")

    pygame.draw.rect(screen, "red", player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        if player.right + player_speed <= screen_width:
            player.x += player_speed
    if key[pygame.K_LEFT]:
        if player.left + player_speed >= 0:
            player.x -= player_speed   
    if key[pygame.K_DOWN]:
        if player.bottom +player_speed <= screen_height:
            player.y += player_speed
    if key[pygame.K_UP]:
        if player.top +player_speed >= 0:
            player.y -= player_speed      

    pygame.display.flip()

print("game over")
