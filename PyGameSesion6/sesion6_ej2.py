import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 600, 400
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

player = pygame.Rect(100, 150, 60, 60)
velocidad = 5

radio = 10
circulo_x = random.randint(radio, ANCHO - radio)
circulo_y = random.randint(radio, ALTO - radio)

contador = 0
fuente = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        player.y -= velocidad
    if teclas[pygame.K_s]:
        player.y += velocidad
    if teclas[pygame.K_a]:
        player.x -= velocidad
    if teclas[pygame.K_d]:
        player.x += velocidad

    dist_x = player.centerx - circulo_x
    dist_y = player.centery - circulo_y
    distancia = (dist_x ** 2 + dist_y ** 2) ** 0.5

    if distancia < radio + player.width / 2:
        contador += 1
        circulo_x = random.randint(radio, ANCHO - radio)
        circulo_y = random.randint(radio, ALTO - radio)

    VENTANA.fill((30, 30, 30))

    pygame.draw.rect(VENTANA, (0, 120, 255), player)
    pygame.draw.circle(VENTANA, (255, 50, 50), (circulo_x, circulo_y), radio)

    texto = fuente.render(f"Objetos recogidos: {contador}", True, (255, 255, 255))
    VENTANA.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
