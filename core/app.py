import pygame
import random
from core.player import Player


class App:
    def __init__(self, resolution_width, resolution_height, player_width, player_height):
        self.running = True
        self.display_surface = None
        self.point_surface = None
        self.player = Player(player_width, resolution_width // 2, resolution_height // 2, player_width, player_height)
        self.resolution_height = resolution_height
        self.resolution_width = resolution_width
        self.player_width = player_width
        self.player_height = player_height
        self.point_coordinates = tuple()

    def startup(self):
        pygame.init()
        pygame.display.set_caption('I.PY_Snake')
        self.spawn_score_point()
        self.running = True
        self.display_surface = pygame.display.set_mode((self.resolution_width, self.resolution_height),
                                                       pygame.HWSURFACE)
        self.point_surface = pygame.Surface((self.player_width / 2, self.player_height / 2))
        pygame.draw.rect(self.point_surface, (255, 255, 255), (0, 0, self.player_width / 2, self.player_height / 2))

    def render(self):
        self.display_surface.fill((0, 0, 0))
        self.player.draw(self.display_surface)
        self.display_surface.blit(self.point_surface, (self.point_coordinates[0], self.point_coordinates[1]))
        pygame.display.flip()

    def spawn_score_point(self):
        self.point_coordinates = (random.uniform(0, self.resolution_width), random.uniform(0, self.resolution_height))

    def execute(self):
        self.startup()
        clock = pygame.time.Clock()
        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

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
            if self.player.collide_with_itself():
                print('Pierdut')
            if self.player.collide_with_point(self.point_surface, self.point_coordinates):
                self.display_surface.fill((0, 0, 0))
                self.spawn_score_point()
                self.player.grow()

            self.render()
            self.player.update()
            clock.tick(10)
        pygame.quit()
