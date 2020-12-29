
class Player:
    speed = 1
    x = 0
    y = 0
    orientation = 0

    def update_player(self):
        if self.orientation == 0:
            self.x = self.x + self.speed
        if self.orientation == 1:
            self.x = self.x - self.speed
        if self.orientation == 2:
            self.y = self.y + self.speed
        if self.orientation == 3:
            self.y = self.y + self.speed
        if self.orientation == 4:
            self.speed = self.y + self.speed

    def move_right(self):
        self.orientation = 0

    def move_left(self):
        self.orientation = 1

    def move_up(self):
        self.orientation = 2

    def move_down(self):
        self.orientation = 3

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_speed(self):
        return self.speed
