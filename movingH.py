import pygame
from obj import Obj


class MovingH(Obj):
    def __init__(self, pos, size, groups):
        super().__init__(pos, size, groups)
        self.image.fill("purple")
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.dir = pygame.math.Vector2((1, 0))
        self.speed = 300

        # self.old_rect = self.rect.copy()

    def update(self, dt):
        self.old_rect = self.rect.copy()  # previous frame
        if self.rect.right > 1000:
            self.rect.right = 1000
            self.pos.x = self.rect.x
            self.dir.x *= -1
        if self.rect.left < 600:
            self.rect.left = 600
            self.pos.x = self.rect.x
            self.dir *= -1

        self.pos.x += self.dir.x * self.speed * dt
        self.rect.x = round(self.pos.x)  # current frame
