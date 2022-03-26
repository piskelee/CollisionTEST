import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups, c_sprites):
        super().__init__(groups)
        # image
        self.image = pygame.Surface((40, 80))
        self.image.fill("blue")

        # pos
        self.rect = self.image.get_rect(topleft=(640, 460))
        self.old_rect = self.rect.copy()

        # moving
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.dir = pygame.math.Vector2()
        self.speed = 500

        self.c_sprites = c_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.dir.y = -1
        elif keys[pygame.K_s]:
            self.dir.y = 1
        else:
            self.dir.y = 0
        if keys[pygame.K_a]:
            self.dir.x = -1
        elif keys[pygame.K_d]:
            self.dir.x = 1
        else:
            self.dir.x = 0

    def collision(self, dir):
        collision_sprites = pygame.sprite.spritecollide(self, self.c_sprites, False)
        if collision_sprites:
            if dir == "h":
                for s in collision_sprites:
                    # check right
                    if self.rect.right >= s.rect.left and self.old_rect.right <= s.old_rect.left:
                        self.rect.right = s.rect.left
                        self.pos.x = self.rect.x

                    # check left
                    if self.rect.left <= s.rect.right and self.old_rect.left >= s.old_rect.right:
                        self.rect.left = s.rect.right
                        self.pos.x = self.rect.x

            if dir == "v":
                for s in collision_sprites:
                    # check bottom
                    if self.rect.bottom >= s.rect.top and self.old_rect.bottom <= s.old_rect.top:
                        self.rect.bottom = s.rect.top
                        self.pos.y = self.rect.y

                    # check top
                    if self.rect.top <= s.rect.bottom and self.old_rect.top >= s.old_rect.bottom:
                        self.rect.top = s.rect.bottom
                        self.pos.y = self.rect.y

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()

        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()

        self.pos.x += self.dir.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision("h")

        self.pos.y += self.dir.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collision("v")

        # self.pos += self.dir * self.speed * dt
        # self.rect.topleft = round(self.pos.x), round(self.pos.y)
