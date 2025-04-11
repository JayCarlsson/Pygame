import pygame
import os

pygame.init

#Define colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Make a clock
clock = pygame.time.Clock()
FPS = 60

# Screen
position = (0,0)
width = 960
height = 540

scroll = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My first game")

#Background images
bg_images = []
for i in range(1, 5):
    bg_image = pygame.image.load("n1/n3/" + str(i) + ".png").convert_alpha()
    bg_image = pygame.transform.scale(bg_image, (width, height))
    bg_images.append(bg_image)

#Character
char_idle = pygame.image.load("Character/Warrior_1/" + "Idle" + ".png").convert_alpha()

#Blit character
def draw_char(x,y):
     screen.blit(char_idle, (x,y))

x = (width * 0.5)
y = (height * 0.5)

#Blit background
def draw_bg():
     for x in range(4):
        speed = 1
        for i in bg_images:
            screen.blit(i, (- scroll * speed, 0))
            speed += 0.2
#Player


#Game loop
run = True
while run:
    
    draw_bg()

    player = screen.blit(char_idle, (100, 100))

# Movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    if key[pygame.K_d] == True:
        player.move_ip(1, 0)

# Close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
















































































































