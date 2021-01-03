import pygame

"""
    Class Player takes care of every logic 
    that involves in our specific case the snake character logic.
    This class keeps track of the variables that define the characteristic 
    of the snake player,variables such as:dimension,boundaries of the 
    map(for computing collisions),spawn coordinates and also the speed
    parameter(step) but maybe the most important role is to apply the logic
    characteristic to the movement of the snake character.
    One of the major role of the Player class besides implementing the logic
    for the movement is to compute the collision between the player and the obstacles
    such as the player's own body,preloaded walls and also the walls of the arena.
"""


class Player:
    # the orientation of the snake player of int type,the value of this variable can be decoded to
    # 0 ->right , 1->left , 2->up , 3->down
    orientation = 0

    def __init__(self, step, spawn_x, spawn_y, width, height, boundary_x, boundary_y):
        """

        :param step: the speed at which our snake-player advances in the map
        :param spawn_x: the x-coordinate of the initial spawn point of the player
        :param spawn_y: the y-coordinate of the initial spawn point of the player
        :param width: the width of the snake-player
        :param height: the height of the snake player
        :param boundary_x: the maximum x at which the player can move safely
        :param boundary_y: the maximum y at which the player can move safely
        """
        self.step = step
        self.segments = list()
        self.width = width
        self.height = height
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y
        # the head segment of the player should spawn at the indicated spawn coordinates
        self.segments.append([spawn_x, spawn_y])
        self.boundary_x = boundary_x
        self.boundary_y = boundary_y
        self.image_surface = pygame.Surface((self.width, self.height))
        pygame.draw.rect(self.image_surface, (255, 255, 255), (0, 0, self.width, self.height))

    def update(self):
        """
            The function update() takes care of the logic involving the snake-player movement.
            Considering the slithering movements which we want to simulate,the approach which we
            adapted was to constantly updating the head of the snake-player by adding the next coordinate on which
            our head should be in one frame and also deleting the last segment of the body.


            The segments which compose our snake player are stored in the list()->segments,in this following manner:
            segments[0] - >The head of the snake player
            segments[1] -> The segment which follows the head of the snake player
            segments[2] -> The segment which follows the segments which follows the snake player

            ...So on and so forth

            segments[n-1] -> The tail of the snake player

            By constantly swapping the head with the tail we ensure that we move by one square,
            also the cases on which we have to take a turn is also taken care of adapting this approach

            [T][x][x][x][H][ ]                          [ ][x->T][x][x][x][H]
            [ ][ ][ ][ ][ ][ ]   ----orientation=0-->   [ ][ ][ ][ ][ ][ ]
            [ ][ ][ ][ ][ ][ ]                          [ ][ ][ ][ ][ ][ ]
            [ ][ ][ ][ ][ ][ ]                          [ ][ ][ ][ ][ ][ ]


        """
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
        """
           The member function grow() takes care of adding another segment in the segments list also
           in the body of the snake player according to its current orientation
        """
        if self.orientation == 0:
            self.segments.append([self.segments[-1][0] + self.step, self.segments[-1][1]])
        if self.orientation == 1:
            self.segments.append([self.segments[-1][0] - self.step, self.segments[-1][1]])
        if self.orientation == 2:
            self.segments.append([self.segments[-1][0], self.segments[-1][1] - self.step])
        if self.orientation == 3:
            self.segments.append([self.segments[-1][0], self.segments[-1][1] + self.step])

    def draw(self, surface):
        """
            The member function draw(surface) use the surface given by the parameter surface to draw a list rectangle
            at the specified coordinates.This function iterate over all the segments and draw them on the required
            surface
            :param surface: a Pygame.Surface object on which we will draw our current segments of the snake player
        """
        for i in range(0, len(self.segments)):
            surface.blit(self.image_surface, (self.segments[i][0], self.segments[i][1]))

    def collide_with_point(self, point_surface, point_coordinates):
        """
            The member function collide_with_point(point_surface,point_coordinates) checks if the current head of the
            snake player collided with a food item called generically point.
            The way this function is doing its job is by making use of the native collision system present in pygame
            engine.The steps which are required is to extract from the surface which represent graphically the object
            its rectangle and check if it collides with other rectangles.
            :param point_surface: surface of the object against which we want to compute the collision
            :param point_coordinates: list() of list() ex:[[20,60]] representing the coordinates of the point on our map
            :return: Boolean value which states if our snake player it is colliding with the rectangle of the point
        """
        player_rect = self.image_surface.get_rect(
            topleft=(self.segments[0][0], self.segments[0][1]))
        point_rect = point_surface.get_rect(
            topleft=(point_coordinates[0], point_coordinates[1]))
        return player_rect.colliderect(point_rect)

    def collide_with_itself(self):
        """
        The member function collide_with_itself() checks if the current head segment of the snake player collided
        with one segment of its own body. The way this function is doing its job is by making use of the native
        collision system present in pygame engine.The steps which are required is to extract from the surface which
        represent graphically the object its rectangle and check if it collides with other rectangles.
        :return: Boolean value which states if our snake player it is colliding with the rectangle of its own segments
        """
        head_rect = self.image_surface.get_rect(
            topleft=(self.segments[0][0], self.segments[0][1]))

        for i in range(1, len(self.segments)):
            body_rect = self.image_surface.get_rect(
                topleft=(self.segments[i][0], self.segments[i][1]))
            if head_rect.colliderect(body_rect):
                return True
        return False

    def collide_with_walls(self):
        """
        The member function collide_with_itself() checks if the current head segment of the snake player collided
        with the boundaries of the map.
        Instead of using the native functionalities from the pygame engine package as we did previously to check for
        collision in the body of the snake player for example we simply check if the coordinates of the head segment
        go over the boundaries of the map
        :return: Boolean value which states if our snake player it is colliding with the boundaries of the map
        """
        head_x = self.segments[0][0]
        head_y = self.segments[0][1]
        if head_x >= self.boundary_x or head_x <= 0 or head_y >= self.boundary_y or head_y < 0:
            return True
        return False

    def collide_with_obstacles(self, obstacle_surface, obstacles_coordinates):
        """
        The member function collide_with_itself() checks if the current head segment of the snake player collideS
        with a set of objects called obstacles.The steps which are required is to extract from the surface which
        represent graphically the object its rectangle and check if it collides with other rectangles.
        :param obstacle_surface: surface of the object of type Pygame.surface on which the object is rendered
        :param obstacles_coordinates: a list of lists which represents the 2D coordinates at which to
                                    aforementioned obstacles can be found
        :return: Boolean value which indicates if our snake player it is colliding with the obstacles
        """
        head_rect = self.image_surface.get_rect(
            topleft=(self.segments[0][0], self.segments[0][1]))
        for i in range(0, len(obstacles_coordinates)):
            obstacle_rect = obstacle_surface.get_rect(
                topleft=(obstacles_coordinates[i][0], obstacles_coordinates[i][1]))
            if head_rect.colliderect(obstacle_rect):
                return True
        return False

    def reset(self):
        """
            The member function reset() resets the player object by deleting all the accumulated segments of the snake
            player.Also it resets the orientation to 0.The player will be again spawned at the spawn_x,spawn_y
            coordinates
        """
        self.orientation = 0
        self.segments.clear()
        self.segments.append([self.spawn_x, self.spawn_y])

    def move_right(self):
        """
            Changes the orientation to 0(Right)
        """
        self.orientation = 0

    def move_left(self):
        """
            Changes the orientation to 1(Left)
        """
        self.orientation = 1

    def move_up(self):
        """
            Changes the orientation to 2(UP)
        """
        self.orientation = 2

    def move_down(self):
        """
            Changes the orientation to 3(Down)
        """
        self.orientation = 3

    def get_segments(self):
        return self.segments

    def get_step(self):
        return self.step
