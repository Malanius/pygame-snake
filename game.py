import pygame

SIZE = 20
WIDTH = 32
HEIGHT = 24

running = True
dead = False
count = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH * SIZE,HEIGHT * SIZE))

# 640 x 480
surface = pygame.image.load("bg.png")

# 20 x 20
character = pygame.image.load("character.png")

snake = [(10,2), (9,2), (8, 2)]
dx, dy = 1, 0

while running:
    # Event hadnling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = 1, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, 1
    
    # Boundary check
    x, y = snake[0]
    if not 0 <= x + dx < WIDTH:
        dead = True
    if not 0 <= y + dy < HEIGHT:
        dead = True

    # Step
    if not dead and count == 10:
        x, y = snake[0]
        snake.insert (0, (x + dx, y + dy))
        snake.pop()
        count = 0

    # Prepare scene
    ##screen.fill((127,0,0))
    screen.blit(surface, (0,0))

    for x, y in snake:
        screen.blit(character, (x * SIZE,y * SIZE))

    # Update the rewritten screen
    pygame.display.update()

    # Cycle tick
    clock.tick(60)
    count += 1