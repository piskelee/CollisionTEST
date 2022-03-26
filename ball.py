import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, c_sprites, player):
        super().__init__(groups)
        self.image = pygame.Surface((40, 40))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=(640, 360))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.dir = pygame.math.Vector2(1, 1)
        self.speed = 800

        self.old_rect = self.rect.copy()

        self.c_sprites = c_sprites
        self.player = player

    def collision(self, dir):
        collision_sprites = pygame.sprite.spritecollide(self, self.c_sprites, False)

        if self.rect.colliderect(self.player.rect):
            collision_sprites.append(self.player)

        if collision_sprites:
            if dir == "h":
                for s in collision_sprites:
                    # check right
                    if self.rect.right >= s.rect.left and self.old_rect.right <= s.old_rect.left:
                        self.rect.right = s.rect.left
                        self.pos.x = self.rect.x
                        self.dir.x *= -1

                    # check left
                    if self.rect.left <= s.rect.right and self.old_rect.left >= s.old_rect.right:
                        self.rect.left = s.rect.right
                        self.pos.x = self.rect.x
                        self.dir.x *= -1

            if dir == "v":
                for s in collision_sprites:
                    # check bottom
                    if self.rect.bottom >= s.rect.top and self.old_rect.bottom <= s.old_rect.top:
                        self.rect.bottom = s.rect.top
                        self.pos.y = self.rect.y
                        self.dir.y *= -1
                    # check top
                    if self.rect.top <= s.rect.bottom and self.old_rect.top >= s.old_rect.bottom:
                        self.rect.top = s.rect.bottom
                        self.pos.y = self.rect.y
                        self.dir.y *= -1

    def win_collision(self, dir):
        if dir == "h":
            if self.rect.left < 0:
                self.rect.left = 0
                self.pos.x = self.rect.x
                self.dir.x *= -1
            if self.rect.right > 1280:
                self.rect.right = 1280
                self.pos.x = self.rect.x
                self.dir.x *= -1

        if dir == "v":
            if self.rect.top < 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
                self.dir.y *= -1
            if self.rect.bottom > 720:
                self.rect.bottom = 720
                self.pos.y = self.rect.y
                self.dir.y *= -1

    def update(self, dt):
        self.old_rect = self.rect.copy()

        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()

        self.pos.x += self.dir.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collision("h")
        self.win_collision("h")

        self.pos.y += self.dir.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collision("v")
        self.win_collision("v")
