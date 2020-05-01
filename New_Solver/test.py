import pygame

pygame.init()
screen = pygame.display.set_mode((800, 100))
running = True
screen.fill((234, 0, 0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
