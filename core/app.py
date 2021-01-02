import pygame
import random
from core.player import Player


class App:
    max_score = 0
    current_round_score = 0

    def __init__(self, rounds, window_width, window_height, player_width, player_height, obstacles):
        self.running = True
        self.display_surface = None
        self.point_surface = None
        self.obstacle_surface = None
        self.obstacles = obstacles
        self.player = Player(player_width, window_width // 2, window_height // 2, player_width,
                             player_height, window_width, window_height)
        self.window_height = window_height
        self.window_width = window_width
        self.player_width = player_width
        self.rounds = rounds
        self.player_height = player_height
        self.point_coordinates = tuple()

    def startup(self):
        pygame.init()
        pygame.display.set_caption('I.PY_Snake')
        self.spawn_score_point()
        self.running = True
        self.display_surface = pygame.display.set_mode((self.window_width, self.window_height),
                                                       pygame.HWSURFACE)
        self.point_surface = pygame.Surface((self.player_width / 2, self.player_height / 2))
        pygame.draw.rect(self.point_surface, (255, 0, 0), (0, 0, self.player_width / 3, self.player_height / 3))
        self.obstacle_surface = pygame.Surface((self.player_width, self.player_height))
        pygame.draw.rect(self.obstacle_surface, (255, 255, 255), (0, 0, self.player_width, self.player_height))

    def render(self):
        self.display_surface.fill((0, 0, 0))
        self.player.draw(self.display_surface)
        self.display_surface.blit(self.point_surface, (self.point_coordinates[0], self.point_coordinates[1]))
        for index in range(0, len(self.obstacles)):
            self.display_surface.blit(self.obstacle_surface, (self.obstacles[index][0], self.obstacles[index][1]))
        pygame.display.flip()

    def render_round_screen(self):
        self.display_surface.fill((0, 0, 0))
        font = pygame.font.Font("assets/pixelated.ttf", 35)
        info_text = font.render(f'Round ended with score:{self.current_round_score}.There are {self.rounds} left', True,
                                (255, 255, 255))
        control_text = font.render('Press ENTER to continue or BACKSPACE to end session', True, (255, 255, 255))
        text_rect = info_text.get_rect(
            center=(self.window_width / 2, self.window_height / 2))
        control_text_rect = control_text.get_rect(
            center=(self.window_width / 2, self.window_height / 2 + text_rect.y))
        self.display_surface.blit(info_text, text_rect)
        self.display_surface.blit(control_text, control_text_rect)
        pygame.display.flip()

    def render_end_screen(self):
        self.display_surface.fill((0, 0, 0))
        font = pygame.font.Font("assets/pixelated.ttf", 35)
        info_text = font.render(f'No rounds left,best overall: {self.max_score}', True, (255, 255, 255))
        control_text = font.render('Press BACKSPACE exit', True, (255, 255, 255))
        text_rect = info_text.get_rect(
            center=(self.window_width / 2, self.window_height / 2))
        control_text_rect = control_text.get_rect(
            center=(self.window_width / 2, self.window_height / 2 + text_rect.y))
        self.display_surface.blit(info_text, text_rect)
        self.display_surface.blit(control_text, control_text_rect)
        pygame.display.flip()

    def spawn_score_point(self):
        self.point_coordinates = (random.uniform(0, self.window_width), random.uniform(0, self.window_height))

    def execute(self):
        self.startup()
        clock = pygame.time.Clock()
        playing = True
        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if playing:
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
                if self.player.collide_with_itself() or self.player.collide_with_walls() \
                        or self.player.collide_with_obstacles(self.obstacle_surface, self.obstacles):
                    self.rounds = self.rounds - 1
                    playing = False
                if self.player.collide_with_point(self.point_surface, self.point_coordinates):
                    self.current_round_score = self.current_round_score + 15
                    self.display_surface.fill((0, 0, 0))
                    self.spawn_score_point()
                    self.player.grow()
                    pygame.display.set_caption(f'I.PY_Snake Score:{self.current_round_score}')
                self.render()
                self.player.update()
            else:
                if self.rounds > 0:
                    pygame.event.pump()
                    keys = pygame.key.get_pressed()
                    if self.current_round_score > self.max_score:
                        self.max_score = self.current_round_score
                    self.render_round_screen()
                    if keys[pygame.K_RETURN]:
                        self.player.reset()
                        self.current_round_score = 0
                        pygame.display.set_caption(f'I.PY_Snake Score:{self.current_round_score}')
                        playing = True
                    if keys[pygame.K_BACKSPACE]:
                        self.rounds = 0
                        playing = False
                else:
                    self.render_end_screen()
                    pygame.event.pump()
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_BACKSPACE]:
                        self.running = False
            clock.tick(11)
