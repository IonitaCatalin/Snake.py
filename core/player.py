import pygame


class Player:
    orientation = 0

    def __init__(self, step, spawn_x, spawn_y, width, height, boundary_x, boundary_y):
        self.step = step
        self.segments = list()
        self.width = width
        self.height = height
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        self.segments.append([spawn_x, spawn_y])
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.image_surface = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.image_surface, (255, 255, 255), (0, 0, self.width, self.height))

    def update(self):
        head = list()

        if self.orientation == 0:
            head.append(self.segments[0][0] + self.step)
            head.append(self.segments[0][1])
        if self.orientation == 1:
            head.append(self.segments[0][0] - self.step)
            head.append(self.segments[0][1])
        if self.orientation == 2:
            head.append(self.segments[0][0])
            head.append(self.segments[0][1] - self.step)
        if self.orientation == 3:
            head.append(self.segments[0][0])
            head.append(self.segments[0][1] + self.step)
        self.segments.insert(0, head)
        self.segments.pop()

    def grow(self):
        if self.orientation == 0:
            self.segments.append([self.segments[-1][0] + self.step, self.segments[-1][1]])
        if self.orientation == 1:
            self.segments.append([self.segments[-1][0] - self.step, self.segments[-1][1]])
        if self.orientation == 2:
            self.segments.append([self.segments[-1][0], self.segments[-1][1] - self.step])
        if self.orientation == 3:
            self.segments.append([self.segments[-1][0], self.segments[-1][1] + self.step])

    def draw(self, surface):
        for i in range(0, len(self.segments)):
            surface.blit(self.image_surface, (self.segments[i][0], self.segments[i][1]))

    def collide_with_point(self, point_surface, point_coordinates):
        player_rect = self.image_surface.get_rect(
            topleft=(self.segments[0][0], self.segments[0][1]))
        point_rect = point_surface.get_rect(
            topleft=(point_coordinates[0], point_coordinates[1]))
        return player_rect.colliderect(point_rect)

    def collide_with_itself(self, ):
        collision = False
        head_rect = self.image_surface.get_rect(
            topleft=(self.segments[0][0], self.segments[0][1]))

        for i in range(1, len(self.segments)):
            body_rect = self.image_surface.get_rect(
                topleft=(self.segments[i][0], self.segments[i][1]))
            if head_rect.colliderect(body_rect):
                collision = True
                break
        return collision

    def collide_with_walls(self):
        head_x = self.segments[0][0]
        head_y = self.segments[0][1]
        if head_x >= self.boundary_x or head_x <= 0 or head_y >= self.boundary_y or head_y < 0:
            return True
        return False

    def reset(self):
        self.orientation = 0
        self.segments.clear()
        self.segments.append([self.spawn_x, self.spawn_y])

    def move_right(self):
        self.orientation = 0

    def move_left(self):
        self.orientation = 1

    def move_up(self):
        self.orientation = 2

    def move_down(self):
        self.orientation = 3

    def get_segments(self):
        return self.segments

    def get_step(self):
        return self.step
