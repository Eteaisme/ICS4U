import pygame
pygame.init()

win = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
circle = pygame.Surface((400,400))
pygame.draw.circle(circle, (255, 255, 255), (80,80), 40)


circleX = 0
circleY = 0
xBallVelocity = 5
yBallVelocity = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    win.fill((0,0,0))
    circleX += xBallVelocity
    circleY += yBallVelocity 

    if(circleX == 700 or circleX == -40):
        xBallVelocity = xBallVelocity * -1 

    if(circleY== 500 or circleY == -40):
        yBallVelocity = yBallVelocity * -1 

    win.blit(circle, (circleX,circleY))
    pygame.display.update()
pygame.quit()
        

