import pygame
import math

pygame.init()

ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

imagen_nave = pygame.image.load("Nave.png").convert()
imagen_nave = pygame.transform.scale(imagen_nave, (80, 80))

pos_x = ANCHO // 2
pos_y = ALTO // 2
velocidad = 4

clock = pygame.time.Clock()
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    dx = mouse_x - pos_x
    dy = mouse_y - pos_y
    angulo = math.degrees(math.atan2(-dy, dx)) - 90

    nave_rotada = pygame.transform.rotate(imagen_nave, angulo)
    rect_nave = nave_rotada.get_rect(center=(pos_x, pos_y))

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        rad = math.radians(angulo + 90)
        pos_x += math.cos(rad) * velocidad
        pos_y -= math.sin(rad) * velocidad
    VENTANA.fill((0, 0, 0))
    VENTANA.blit(nave_rotada, rect_nave)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
