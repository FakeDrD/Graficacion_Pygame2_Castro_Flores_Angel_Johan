import pygame
reloj = pygame.time.Clock()
pygame.init()

ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))

blanco = (255, 255, 255)
azul = (0, 0, 255)

x, y = 50, ALTO/2
velocidad = 1

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    ventana.fill(blanco)
    pygame.draw.circle(ventana, azul, (x, y),50)
    pygame.display.flip()
    x+=velocidad
    if x >= ANCHO-50:
        velocidad+=1
        velocidad*=-1
    elif x <= 50:
        velocidad+=-1
        velocidad*=-1
    reloj.tick(60)  # 60 FPS
pygame.quit()