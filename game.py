import pygame

running = True

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))

# 640 x 480
surface = pygame.image.load("bg.png")

# 20 x 20
character = pygame.image.load("character.png")

SIZE = 20
x = 1
y = 2

while running:
    # Event hadnling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                x -= 1
            elif event.key == pygame.K_RIGHT:
                x += 1
            elif event.key == pygame.K_UP:
                y -= 1
            elif event.key == pygame.K_DOWN:
                y += 1
    
    # Prepare scene
    ##screen.fill((127,0,0))

    screen.blit(surface, (0,0))
    screen.blit(character, (x * SIZE,y * SIZE))

    # Update the rewritten screen
    pygame.display.update()

    # Cycle tick
    clock.tick(60)