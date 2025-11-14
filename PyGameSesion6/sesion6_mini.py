import pygame
import random
import sys
import math

pygame.init()

ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

fuente = pygame.font.SysFont(None, 36)

# Nave jugador
imagen_nave_original = pygame.image.load("nave.png").convert_alpha()
imagen_nave_original = pygame.transform.scale(imagen_nave_original, (60, 60))
pos_x = ANCHO // 2
pos_y = ALTO - 80
velocidad = 5

HITBOX_FACTOR = 0.55

# Obstáculos
num_obstaculos = 5
radio_obs = 20
obstaculos = []
for _ in range(num_obstaculos):
    x = random.randint(radio_obs, ANCHO - radio_obs)
    y = random.randint(radio_obs, ALTO - radio_obs)
    vx = random.choice([-3, 3])
    vy = random.choice([-3, 3])
    obstaculos.append({"pos": [x, y], "vx": vx, "vy": vy})

# Objetos a recoger
radio_obj = 15
obj_x = random.randint(radio_obj, ANCHO - radio_obj)
obj_y = random.randint(radio_obj, ALTO - radio_obj)

puntos = 0
clock = pygame.time.Clock()
running = True

def reiniciar_juego():
    global pos_x, pos_y, obstaculos, puntos
    pos_x = ANCHO // 2
    pos_y = ALTO - 80
    puntos = 0
    obstaculos.clear()
    for _ in range(num_obstaculos):
        x = random.randint(radio_obs, ANCHO - radio_obs)
        y = random.randint(radio_obs, ALTO - radio_obs)
        vx = random.choice([-3, 3])
        vy = random.choice([-3, 3])
        obstaculos.append({"pos": [x, y], "vx": vx, "vy": vy})

# Diccionario de combinaciones de teclas y ángulos
ROTACIONES = {
    (pygame.K_w,): 0,
    (pygame.K_d,): -90,
    (pygame.K_s,): 180,
    (pygame.K_a,): 90,
    (pygame.K_w, pygame.K_d): -45,
    (pygame.K_w, pygame.K_a): 45,
    (pygame.K_s, pygame.K_a): 135,
    (pygame.K_s, pygame.K_d): -135
}

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    dx_move = 0
    dy_move = 0
    keys_pressed = []

    if teclas[pygame.K_w]:
        dy_move -= velocidad
        keys_pressed.append(pygame.K_w)
    if teclas[pygame.K_s]:
        dy_move += velocidad
        keys_pressed.append(pygame.K_s)
    if teclas[pygame.K_a]:
        dx_move -= velocidad
        keys_pressed.append(pygame.K_a)
    if teclas[pygame.K_d]:
        dx_move += velocidad
        keys_pressed.append(pygame.K_d)

    pos_x += dx_move
    pos_y += dy_move

    # Limitar dentro de la pantalla
    pos_x = max(0, min(pos_x, ANCHO - imagen_nave_original.get_width()))
    pos_y = max(0, min(pos_y, ALTO - imagen_nave_original.get_height()))

    # Determinar la rotación según teclas
    angulo = 0
    for combo, ang in ROTACIONES.items():
        if all(teclas[k] for k in combo) and len(combo) == len(keys_pressed):
            angulo = ang
            break

    imagen_nave = pygame.transform.rotate(imagen_nave_original, angulo)
    rect_nave = imagen_nave.get_rect(center=(pos_x + imagen_nave_original.get_width()/2,
                                             pos_y + imagen_nave_original.get_height()/2))

    # Hitbox reducida
    hitbox_width = rect_nave.width * HITBOX_FACTOR
    hitbox_height = rect_nave.height * HITBOX_FACTOR
    hitbox = pygame.Rect(0, 0, hitbox_width, hitbox_height)
    hitbox.center = rect_nave.center

    # Actualizar obstáculos
    for obs in obstaculos:
        obs["pos"][0] += obs["vx"]
        obs["pos"][1] += obs["vy"]

        if obs["pos"][0] - radio_obs <= 0 or obs["pos"][0] + radio_obs >= ANCHO:
            obs["vx"] *= -1
        if obs["pos"][1] - radio_obs <= 0 or obs["pos"][1] + radio_obs >= ALTO:
            obs["vy"] *= -1

    # Colisiones
    for obs in obstaculos:
        dx = hitbox.centerx - obs["pos"][0]
        dy = hitbox.centery - obs["pos"][1]
        distancia = math.hypot(dx, dy)
        if distancia < radio_obs + hitbox.width/2:
            reiniciar_juego()
            break

    dx_obj = hitbox.centerx - obj_x
    dy_obj = hitbox.centery - obj_y
    distancia_obj = math.hypot(dx_obj, dy_obj)
    if distancia_obj < radio_obj + hitbox.width/2:
        puntos += 1
        obj_x = random.randint(radio_obj, ANCHO - radio_obj)
        obj_y = random.randint(radio_obj, ALTO - radio_obj)

    # Dibujar todo
    VENTANA.fill((20, 20, 30))
    VENTANA.blit(imagen_nave, rect_nave.topleft)
    pygame.draw.circle(VENTANA, (255, 50, 50), (int(obj_x), int(obj_y)), radio_obj)
    for obs in obstaculos:
        pygame.draw.circle(VENTANA, (255, 150, 0), (int(obs["pos"][0]), int(obs["pos"][1])), radio_obs)

    texto = fuente.render(f"Puntos: {puntos}", True, (255, 255, 255))
    VENTANA.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
