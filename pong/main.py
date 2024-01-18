import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

bola_x, bola_y = WIDTH // 2, HEIGHT // 2
vel_bola_x, vel_bola_y = BALL_SPEED, BALL_SPEED

barra_width, barra_height = 15, 60
barra_esq_x, barra_dir_x = 10, WIDTH - 25
barra_esq_y, barra_dir_y = HEIGHT // 2 - barra_height // 2, HEIGHT // 2 - barra_height // 2 
vel_barra = 7
score_left, score_right = 0, 0

# Fonte para exibir a pontuação
fonte = pygame.font.Font(None, 36)

def reset_bola():
    return WIDTH // 2, HEIGHT // 2, BALL_SPEED, BALL_SPEED

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and barra_esq_y > 0:
            barra_esq_y -= vel_barra
        if keys[pygame.K_s] and barra_esq_y < HEIGHT - barra_height:
            barra_esq_y += vel_barra
        if keys[pygame.K_UP] and barra_dir_y > 0:
            barra_dir_y -= vel_barra
        if keys[pygame.K_DOWN] and barra_dir_y < HEIGHT - barra_height:
            barra_dir_y += vel_barra

        bola_x += vel_bola_x
        bola_y += vel_bola_y

        if (
            barra_esq_x < bola_x < barra_esq_x + barra_width
            and barra_esq_y < bola_y < barra_esq_y + barra_height
        ) or (
            barra_dir_x < bola_x < barra_dir_x + barra_width
            and barra_dir_y < bola_y < barra_dir_y + barra_height
        ):
            vel_bola_y = -vel_bola_x

        if bola_y <= 0 or bola_y >= HEIGHT:
            vel_bola_y = -vel_bola_y

        if bola_x <= 0:
            score_right += 1



