import pygame

from player import Player
from settings import HEIGHT, WIDTH

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player((0, HEIGHT // 2))


def main():
    run = True

    while run:
        dt = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        window.fill("Black")
        window.blit(player.img, player.rect)
        player.move(dt)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
