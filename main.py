import pygame
import sys


def __init__(self, x: int | float, y: int | float, color: list[int] | tuple[int], r: int = 5, direction: int | float = -1):
        self.x = x
        self.y = y
        self.color = color
        self.r = r
        if direction == -1:
            self.d = ri(0, 360)
        else:
            self.d = direction


def move(self, speed):
        self.x += sin(self.d / 180 * pi) * speed
        self.y += cos(self.d / 180 * pi) * speed
        if self.x > W - self.r or self.x < 0 + self.r:
            self.d = 360 - self.d
        if self.y > H - self.r or self.y < 0 + self.r:
            self.d = 540 - self.d
            if self.d >= 360:
                self.d -= 360
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

# Game loop
while gameIsRunning:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False
        if event.type == 


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (100, 100), 20)
    # Flip the display
    pygame.display.flip()

    # Limit the frame rate to 30 FPS
    clock.tick(FPS)


pygame.quit()
sys.exit()