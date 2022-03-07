import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score = 0
score_surface = test_font.render(str(score), False, (64,64,64))
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))
snail_vel = 4
snail_accel = 0.01

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0
player_gravity_increase = 0.1

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rectangle.bottom == 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                score = 0
                score_surface = test_font.render(str(score), False, (64,64,64))
                snail_vel = 4
                player_gravity_increase = 0.1


    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(score_surface, score_rect)

        snail_rectangle.x -= snail_vel
        snail_vel += snail_accel
        if snail_rectangle.right <= 0:
            snail_rectangle.left = 800
            score += 1
            score_surface = test_font.render(str(score), False, (64,64,64))
            player_gravity_increase += 0.01

        screen.blit(snail_surface, snail_rectangle)

        player_gravity += 1 + player_gravity_increase
        player_rectangle.y += player_gravity

        if player_rectangle.bottom > 300:
            player_rectangle.bottom = 300

        screen.blit(player_surface, player_rectangle)

        if player_rectangle.colliderect(snail_rectangle):
            game_active = False
    else:
        screen.fill((200,200,200))


    pygame.display.update()
    clock.tick(60)
