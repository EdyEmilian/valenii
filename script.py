import pygame
import sys
from pygame.locals import *
import random

pygame.init()

screen = pygame.display.set_mode((710, 390))
pygame.display.set_caption("salut zarna")

image = pygame.image.load("Screenshot_92.png")

game_running = True

player_image = pygame.image.load("Screenshot_97.png")
playerX = 300
playerY = 300
player_speed = 5

diriga_food = pygame.image.load("images.png")

food_Width = diriga_food.get_width()
food_height = diriga_food.get_height()
foodX = random.randint(0, 710 - food_Width)
foodY = random.randint(0, 390 - food_height)

score = 0

player_width = player_image.get_width()
player_height = player_image.get_height()

pygame.mixer.music.load("aiputamica.mp3")
pygame.mixer.music.play(loops=1000, start=0.0, fade_ms=0)

clock = pygame.time.Clock()

while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerY -= player_speed
    if keys[pygame.K_s]:
        playerY += player_speed
    if keys[pygame.K_a]:
        playerX -= player_speed
    if keys[pygame.K_d]:
        playerX += player_speed

    if playerX < 0:
        playerX = 0
    if playerX > 710 - player_width:
        playerX = 710 - player_width
    if playerY < 0:
        playerY = 0
    if playerY > 390 - player_height:
        playerY = 390 - player_height


    player_rect = pygame.Rect(playerX, playerY, player_width, player_height)
    food_rect = pygame.Rect(foodX, foodY, food_Width, food_height)

    if player_rect.colliderect(food_rect):
        score += 1
        foodX = random.randint(0, 710 - food_Width)
        foodY = random.randint(0, 390 - food_height)

    screen.blit(image, (0, 0))
    screen.blit(player_image, (playerX, playerY))
    
    font = pygame.font.Font(None, 36)
    text = font.render(f"score: {score}", True, (0, 0, 0))
    screen.blit(text, (0, 0))

    screen.blit(diriga_food, (foodX, foodY))


    
    pygame.display.update()
    clock.tick(60)