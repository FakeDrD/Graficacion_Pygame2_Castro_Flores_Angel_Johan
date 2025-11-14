import pygame
reloj = pygame.time.Clock()
pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)

x, y = ANCHO/2, 50
velocidad = 0

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    y+=velocidad
    velocidad+=0.5
    if y >= ALTO-50:
        y= ALTO-50
        if abs((velocidad-(velocidad*.20))*-1) < 5:
            velocidad = 0
        else:
            velocidad = (velocidad-(velocidad*.20))*-1
    reloj.tick(60)  # 60 FPS
    ventana.fill(blanco)
    pygame.draw.circle(ventana, azul, (x, y),50)
    pygame.display.flip()
pygame.quit()