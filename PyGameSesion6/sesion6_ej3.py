import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 600, 400
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

player = pygame.Rect(ANCHO//2 - 25, ALTO - 60, 50, 50)
velocidad = 5

num_obstaculos = 5
radio = 20
obstaculos = []
for _ in range(num_obstaculos):
    x = random.randint(radio, ANCHO - radio)
    y = random.randint(50, ALTO - 150)
    vx = random.choice([-3, 3])  
    obstaculos.append({"pos": [x, y], "vx": vx})

clock = pygame.time.Clock()
running = True

def reiniciar_juego():
    global player, obstaculos
    player.x = ANCHO//2 - 25
    player.y = ALTO - 60
    obstaculos = []
    for _ in range(num_obstaculos):
        x = random.randint(radio, ANCHO - radio)
        y = random.randint(50, ALTO - 150)
        vx = random.choice([-3, 3])
        obstaculos.append({"pos": [x, y], "vx": vx})

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

    player.x = max(0, min(player.x, ANCHO - player.width))
    player.y = max(0, min(player.y, ALTO - player.height))

    for obs in obstaculos:
        obs["pos"][0] += obs["vx"]
        if obs["pos"][0] - radio <= 0 or obs["pos"][0] + radio >= ANCHO:
            obs["vx"] *= -1

    for obs in obstaculos:
        dx = player.centerx - obs["pos"][0]
        dy = player.centery - obs["pos"][1]
        distancia = (dx**2 + dy**2)**0.5
        if distancia < radio + player.width/2:
            reiniciar_juego()
            break

    VENTANA.fill((30, 30, 30))
    pygame.draw.rect(VENTANA, (0, 120, 255), player)
    for obs in obstaculos:
        pygame.draw.circle(VENTANA, (255, 50, 50), (int(obs["pos"][0]), int(obs["pos"][1])), radio)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
