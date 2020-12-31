class Player:
    segments = []
    orientation = 0
    updateCounter = 0
    updateCounterMax = 2

    def __init__(self, step):
        self.step = step
        self.segments.append([0, 0])
        print(self.segments)

    def update(self):
        self.updateCounter = self.updateCounter + 1
        if self.updateCounter > self.updateCounterMax:
            if len(self.segments) > 0:
                for i in range(len(self.segments) - 1, 0, -1):
                    self.segments[i] = self.segments[i - 1]
            if self.orientation == 0:
                print(self.segments)
                self.segments[0][0] = self.segments[0][0] + self.step
            if self.orientation == 1:
                self.segments[0][0] = self.segments[0][0] - self.step
            if self.orientation == 2:
                self.segments[0][1] = self.segments[0][1] - self.step
            if self.orientation == 3:
                self.segments[0][1] = self.segments[0][1] + self.step
            self.updateCounter = 0

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
