import pygame
from core.player import Player


class App:
    def __init__(self, width, height):
        self.running = True
        self.display_surface = None
        self.image_surface = None
        self.player = Player()
        self.height = height
        self.width = width

    def prepare_startup(self):
        pygame.init()
        pygame.display.set_caption('I.PY_Snake')
        self.display_surface = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        self.running = True
        self.image_surface = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.image_surface, (255, 255, 255), (200, 150, 100, 50))

    def render_player(self):
        self.display_surface.fill((0, 0, 0))
        self.display_surface.blit(self.image_surface, (self.player.get_x(), self.player.get_y()))
        pygame.display.flip()

    def execute(self):
        self.prepare_startup()

        while self.running:
            self.render_player()
