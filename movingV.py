import pygame

from obj import Obj


class MovingV(Obj):
    def __init__(self, pos, size, groups):
        super().__init__(pos, size, groups)
        self.image.fill("green")
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.dir = pygame.math.Vector2((0, 1))
        self.speed = 350

        # self.old_rect = self.rect.copy()

    def update(self, dt):
        self.old_rect = self.rect.copy()
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.pos.y = self.rect.y
            self.dir.y *= -1
        if self.rect.bottom < 120:
            self.rect.bottom = 120
            self.pos.y = self.rect.y
            self.dir.y *= -1

        self.pos.y += self.dir.y * self.speed * dt
        self.rect.y = round(self.pos.y)
