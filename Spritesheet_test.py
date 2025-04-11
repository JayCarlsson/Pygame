import pygame
import Spritesheet

pygame.init()

width = 960
height = 540

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spritesheet")

sprite_sheet_image = pygame.image.load("Character/Warrior_1/" + "idle" + ".png").convert_alpha()
sprite_sheet = Spritesheet.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
BLACK = (0, 0, 0)

#Create animation list
animation_list = []
animation_steps = 4
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 175
frame = 0
step_counter = 0

for animation in range(animation_steps):
    for _ in range (animation):
        animation_list.append(sprite_sheet.get_image(step_counter, 96, 96, 2, BLACK))
        step_counter += 1

run = True
while run:

    #update background
    screen.fill(BG)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    #show frame image
    screen.blit(animation_list[frame], (0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()