import pygame

pygame.init()
ANCHO, ALTO = 600, 400
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

sprite_sheet = pygame.image.load("PyGame5.2.png").convert_alpha()

NUM_FRAMES = 6
FRAME_ANCHO = sprite_sheet.get_width() // NUM_FRAMES
FRAME_ALTO = sprite_sheet.get_height()

frames = []
for i in range(NUM_FRAMES):
    frame = sprite_sheet.subsurface(pygame.Rect(i * FRAME_ANCHO, 0, FRAME_ANCHO, FRAME_ALTO))
    frame = pygame.transform.scale(frame, (FRAME_ANCHO * 2, FRAME_ALTO * 2))  # ESCALAR X2
    frames.append(frame)

frame_index = 0
tiempo_animacion = 100
ultimo_cambio = pygame.time.get_ticks()

clock = pygame.time.Clock()
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_cambio >= tiempo_animacion:
        frame_index = (frame_index + 1) % NUM_FRAMES
        ultimo_cambio = tiempo_actual

    VENTANA.fill((30, 30, 30))
    frame_actual = frames[frame_index]
    ancho_f = frame_actual.get_width()
    alto_f = frame_actual.get_height()
    
    VENTANA.blit(frame_actual, (ANCHO//2 - ancho_f//2, ALTO//2 - alto_f//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
