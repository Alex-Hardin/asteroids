import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Sets up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Return
        # fill screen display with black https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
        screen.fill((0,0,0))
        # update the display  https://www.pygame.org/docs/ref/display.html#pygame.display.flip
        pygame.display.flip()

if __name__ == "__main__":
    main()