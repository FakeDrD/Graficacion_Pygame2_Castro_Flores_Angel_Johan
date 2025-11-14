import pygame
import sys

pygame.init()

ANCHO, ALTO = 600, 400
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

player = pygame.Rect(100, 150, 60, 60)
color_player = (0, 0, 255)

objetivo = pygame.Rect(ANCHO/2 - 25, ALTO/2 - 25, 50, 50)
color_objetivo = (255, 0, 0)

velocidad = 5
clock = pygame.time.Clock()
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()


    prev_x = player.x
    prev_y = player.y

    if teclas[pygame.K_w]:
        player.y -= velocidad
    if teclas[pygame.K_s]:
        player.y += velocidad
    if teclas[pygame.K_a]:
        player.x -= velocidad
    if teclas[pygame.K_d]:
        player.x += velocidad

    if player.colliderect(objetivo):
        player.x = prev_x
        player.y = prev_y
        color_player = (0, 255, 0)
    else:
        color_player = (0, 0, 255)

    VENTANA.fill((30, 30, 30))
    pygame.draw.rect(VENTANA, color_player, player)
    pygame.draw.rect(VENTANA, color_objetivo, objetivo)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
