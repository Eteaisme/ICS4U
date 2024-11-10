import pygame
import random

# Initialize pygame
pygame.init()

# Set screen dimensions 
WIDTH, HEIGHT = 1000, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Color variables 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
paddleWidth, paddleHeight = 20,100
ballVelocityX, ballVelocityY  = 5,5
ballRadius = 15
paddleVelocity = 7
rightScore, leftScore = 0,0

# Create paddle and ball
leftPaddle = pygame.Rect(30, HEIGHT // 2 - paddleHeight // 2, paddleWidth, paddleHeight)
rightPaddle = pygame.Rect(WIDTH - 50, HEIGHT // 2 - paddleHeight // 2, paddleWidth, paddleHeight)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, ballRadius* 2, ballRadius* 2)

# Game 
running = True
frames = pygame.time.Clock()

# Font for displaying score
font = pygame.font.Font(None, 36)

def updateScreen():
    window.fill(BLACK)  
    #Draw paddles and ball
    pygame.draw.rect(window, WHITE, leftPaddle)  
    pygame.draw.rect(window, WHITE, rightPaddle)  
    pygame.draw.ellipse(window, WHITE, ball)  
    
    # Write the scores
    score = font.render(f"{leftScore}   {rightScore}", True, WHITE)
    window.blit(score, (WIDTH // 2 - score.get_width() // 2, 20))
    
    pygame.display.flip()

def ballMovement():
    global ballVelocityX, ballVelocityY, leftScore,rightScore 
    
    # Update ball position
    ball.x += ballVelocityX
    ball.y += ballVelocityY
    
    # Handle wall collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ballVelocityY  *= -1
    
    # Left paddle collision
    if ball.colliderect(leftPaddle) and ballVelocityX < 0:
        ballVelocityX  *= -1
    
    # Right paddle collision
    if ball.colliderect(rightPaddle) and ballVelocityX > 0:
        ballVelocityX *= -1
    
    # Scoring 
    if ball.left <= 0:
        leftScore += 1
        resetBall()
    elif ball.right >= WIDTH:
        rightScore += 1
        resetBall()

def resetBall():
    global ballVelocityX, ballVelocityY
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ballVelocityX *= random.choice([-1, 1])
    ballVelocityY *= random.choice([-1, 1])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Check inputs
    keys = pygame.key.get_pressed()
    # Left paddle 
    if keys[pygame.K_w] and leftPaddle.top > 0:
        leftPaddle.y -= paddleVelocity
    if keys[pygame.K_s] and leftPaddle.bottom < HEIGHT:
        leftPaddle.y += paddleVelocity 

    # Right paddle 
    if keys[pygame.K_UP] and rightPaddle.top > 0:
        rightPaddle.y -=  paddleVelocity
    if keys[pygame.K_DOWN] and rightPaddle.bottom < HEIGHT:
        rightPaddle.y +=  paddleVelocity
    
    
    ballMovement()
    updateScreen()
    
    # Set frame rate
    frames.tick(120)

pygame.quit()
 