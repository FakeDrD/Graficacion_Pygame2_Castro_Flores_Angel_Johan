import pygame
reloj = pygame.time.Clock()
pygame.init()

ANCHO, ALTO, radio = 800, 600, 20
ventana = pygame.display.set_mode((ANCHO, ALTO))

blanco = (255, 255, 255)
azul = (0, 0, 255)
x, y, z = ANCHO/2, ALTO/2, 0
velocidad = 1

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill(blanco)
    pygame.draw.circle(ventana, azul, (x, y),radio)
    pygame.display.flip()
    radio+=z
    if radio == 50:
        z =-1
    elif radio == 20:
        z = 1
    reloj.tick(60)  # 60 FPS
pygame.quit()