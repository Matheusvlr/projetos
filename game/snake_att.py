import pygame
import random

# Inicializando o pygame
pygame.init()

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
preto = (0, 0, 0)

# Criação da janela
screen_width = 900
screen_height = 600
janela_jogo = pygame.display.set_mode((screen_width, screen_height))

# Título do jogo
pygame.display.set_caption('Jogo da cobrinha')
pygame.display.update()
tempo = pygame.time.Clock()
fonte = pygame.font.SysFont(None, 55)

def tela_texto(text, color, x, y):
    texto_tela = fonte.render(text, True, color) 
    janela_jogo.blit(texto_tela, [x,y])

def snake(janela_jogo, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(janela_jogo, color, [x, y, snake_size, snake_size])

# Loop do jogo
def gameloop():
    exite_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    # Adicionando buffer para a comida
    buffer = 50
    food_x = random.randint(buffer, screen_width - buffer)
    food_y = random.randint(buffer, screen_height - buffer)

    score = 0
    init_velocity = 5
    snake_size = 25
    food_size = 15  # Tamanho da comida
    fps = 60
    
    while not exite_game:
        if game_over:
            janela_jogo.fill(branco)
            tela_texto('Game Over! Pressione Enter para continuar', vermelho, 50, 100, )
            pygame.display.update()  # Atualizando a tela para mostrar a mensagem de Game Over

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exite_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exite_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) <6 and abs(snake_y - food_y) <6:
                score += 1
                food_x = random.randint(buffer, screen_width - buffer)
                food_y = random.randint(buffer, screen_height - buffer)
                snk_length += 5

            janela_jogo.fill(branco)
            tela_texto("Pontuação: " + str(score * 10), vermelho, 5, 5)
            pygame.draw.rect(janela_jogo, vermelho, [food_x, food_y, food_size, food_size])  # Desenhar a comida usando food_size
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x <0 or snake_x > screen_width or snake_y <0 or snake_y > screen_height:
                game_over = True

            snake(janela_jogo, preto, snk_list, snake_size)
            pygame.display.update()

            tempo.tick(fps)
    
gameloop()