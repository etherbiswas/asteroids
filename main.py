import pygame
from constants import *  # Make sure SCREEN_WIDTH and SCREEN_HEIGHT are defined in constants.py

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_color = pygame.Color("#1d2021")  # Using hex code directly

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with the background color
        screen.fill(background_color)

        # Update the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
