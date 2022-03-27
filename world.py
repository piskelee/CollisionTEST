import pygame
from obj import Obj
from movingH import MovingH
from movingV import MovingV
from ball import Ball
from player import Player


class World:
    def __init__(self):
        # get screen
        self.screen = pygame.display.get_surface()

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.c_sprites = pygame.sprite.Group()

        # sprites setup
        Obj((100, 300), (100, 50), [self.all_sprites, self.c_sprites])
        Obj((800, 600), (100, 200), [self.all_sprites, self.c_sprites])
        Obj((900, 200), (200, 10), [self.all_sprites, self.c_sprites])
        MovingV((200, 300), (200, 60), [self.all_sprites, self.c_sprites])
        MovingH((850, 350), (100, 100), [self.all_sprites, self.c_sprites])
        self.player = Player(self.all_sprites, self.c_sprites)
        ball = Ball(self.all_sprites, self.c_sprites, self.player)

    def update(self, dt):
        self.screen.fill("black")
        self.all_sprites.update(dt)

        for s in self.all_sprites:
            pygame.draw.rect(self.screen, 'white', s.old_rect)

        self.all_sprites.draw(self.screen)
