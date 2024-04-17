import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen = pygame.display.set_mode((800, 600))

# Set the title of the window
pygame.display.set_caption("My Game")

# Set the FPS
FPS = 30
clock = pygame.time.Clock()

gameIsRunning = True

x = 100
y = 100
speedx = 5
speedy = 5
# Game loop
while gameIsRunning:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

		# Clear the screen
    screen.fill((0, 0, 0))
    
    x += speedx
    y += speedy
    pygame.draw.circle(screen, (255, 255, 255), (x , y ), 20)

    # if x+20 >= 800 or x-20 <= 0:
    #     speedx = -speedx
    # elif y+20 >= 600 or y-20 <= 0:
    #     speedy = -speedy

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS
    clock.tick(FPS)


pygame.quit()
sys.exit()