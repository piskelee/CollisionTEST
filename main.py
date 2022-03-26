import sys
import time
import pygame
from world import World


class Game:
    def __init__(self):
        # setup
        pygame.init()
        pygame.display.set_caption("Collision Test")
        self.screen = pygame.display.set_mode((1280, 720))
        self.world = World()

    def run(self):
        # FPS setup
        last_time = time.time()

        # game loops
        while True:
            # FPS
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # objects join
            self.screen.fill("white")
            self.world.update(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
