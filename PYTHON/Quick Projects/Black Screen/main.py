import pygame
import sys
import os

pygame.init()

# Get the directory where this script is located
base_path = os.path.dirname(__file__)
image_path = os.path.join(base_path, "Black.jpg")

# Create fullscreen window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Hide mouse cursor
pygame.mouse.set_visible(False)

# Load and scale image once
image = pygame.image.load(image_path).convert()
image = pygame.transform.scale(image, screen.get_size())

# Draw once
screen.blit(image, (0, 0))
pygame.display.flip()

# Ultra-low CPU event loop
running = True
while running:
    event = pygame.event.wait()  # waits (no constant polling)

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False

pygame.quit()
sys.exit()
