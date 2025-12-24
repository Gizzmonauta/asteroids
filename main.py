import pygame
from constants import *
from logger import *
from player import *


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyr = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        dt = clock.tick(60) / 1000.0
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        screen.fill("black")
        pyr.update(dt)
        pyr.draw(screen)
        pygame.display.flip()
        print(f"Delta time: {dt} seconds")



if __name__ == "__main__":
    main()
