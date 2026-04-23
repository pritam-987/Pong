import pygame

from settings import *


class Player:
    def __init__(self, pos):
        self.img = pygame.Surface((player_width, player_height))
        self.img.fill("White")
        self.rect = self.img.get_rect(center=pos)
        self.speed = 200
        self.y = float(self.rect.y)

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.y += self.speed * dt
        if keys[pygame.K_w]:
            self.y -= self.speed * dt
        self.rect.y = int(self.y)
