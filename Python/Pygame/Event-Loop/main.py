# Import and start pygame
import pygame
pygame.init()

def getMousePosition():
    return pygame.mouse.get_pos()

window = pygame.display.set_mode((1000, 1000))
frames = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("The A key was pressed!")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("The mouse was clicked!")
    
    frames.tick(60)
    window.fill((0, 0, 0))
    
    # Draw the circle at the current mouse position
    mouse_x, mouse_y = getMousePosition()
    pygame.draw.circle(window, (255, 255, 255), (mouse_x, mouse_y), 40)
    
    pygame.display.update()

pygame.quit()
