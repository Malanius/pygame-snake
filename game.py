import pygame

running = True
count = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))

# 640 x 480
surface = pygame.image.load("bg.png")

# 20 x 20
character = pygame.image.load("character.png")

SIZE = 20
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
    
    # Step
    if count == 30:
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