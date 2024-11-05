import pygame
pygame.init()

win = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    win.fill((255,0,0))
    pygame.display.update()
pygame.quit()
        

