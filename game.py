import pygame

running = True

clock = pygame.time.Clock()
pygame.display.set_mode((640,480))

while running:
    # Event hadnling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    # Cycle tick
    clock.tick(60)