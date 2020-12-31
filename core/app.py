import pygame
import time

from core.player import Player


class App:
    def __init__(self, resolution_width, resolution_height, player_width, player_height):
        self.running = True
        self.display_surface = None
        self.image_surface = None
        self.player = Player(10)
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width
        self.player_width = player_width
        self.player_height = player_height

    def prepare_startup(self):
        pygame.init()
        pygame.display.set_caption('I.PY_Snake')
        self.running = True
        self.display_surface = pygame.display.set_mode((self.resolution_width, self.resolution_height), pygame.HWSURFACE)
        self.image_surface = pygame.Surface((self.player_width, self.player_height))
        pygame.draw.rect(self.image_surface, (255, 255, 255), (0, 0, self.player_width,self.player_height))

    def render_assets(self):
        self.display_surface.fill((0, 0, 0))
        player_segments = self.player.get_segments()
        for i in range(0, len(player_segments)):
            print(i)
            self.display_surface.blit(self.image_surface, (player_segments[i][0], player_segments[i][1]))
        pygame.display.flip()

    def execute(self):
        self.prepare_startup()

        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.player.move_right()
            if keys[pygame.K_LEFT]:
                self.player.move_left()
            if keys[pygame.K_UP]:
                self.player.move_up()
            if keys[pygame.K_DOWN]:
                self.player.move_down()
            if keys[pygame.K_ESCAPE]:
                self.running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.player.update()
            self.render_assets()
            time.sleep(50.0 / 1000.0)
        pygame.quit()
