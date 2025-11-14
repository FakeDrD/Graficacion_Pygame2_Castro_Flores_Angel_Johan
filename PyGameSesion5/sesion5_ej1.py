import pygame

pygame.init()

ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
imagen_original = pygame.image.load("PyGame5.1.jpg").convert_alpha()

ancho_img, alto_img = imagen_original.get_size()
escala = 0.5  

reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_PLUS or evento.key == pygame.K_KP_PLUS:  
                escala += 0.1
            elif evento.key == pygame.K_MINUS or evento.key == pygame.K_KP_MINUS:
                escala -= 0.1
                if escala < 0.1:  
                    escala = 0.1

    nuevo_ancho = int(ancho_img * escala)
    nuevo_alto = int(alto_img * escala)
    imagen_redimensionada = pygame.transform.smoothscale(imagen_original, (nuevo_ancho, nuevo_alto))

    ventana.fill((0, 0, 0))

    x = (ANCHO - nuevo_ancho) // 2
    y = (ALTO - nuevo_alto) // 2
    ventana.blit(imagen_redimensionada, (x, y))

    pygame.display.flip()
    reloj.tick(60)
