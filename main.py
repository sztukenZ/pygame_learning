import pygame
from sys import exit

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Runner")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # Draw all our elements
        # Update everything
        pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
