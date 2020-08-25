import pygame

WHITE = (255, 255, 255)


class Shot:
    def __init__(self, matrix_position, direction, max_distance, damage):
        if direction == Direction.DOWN or direction == Direction.UP:
            self.picture = pygame.image.load("pictures/vertical_shot.png")
        else:
            self.picture = pygame.image.load("pictures/horizontal_shot.png")
        self.direction = direction
        self.picture.set_colorkey(WHITE)
        self.position = matrix_position
        self.max_distance = max_distance
        self.distance_traveled = 0
        self.damage = damage

    def get_position(self):
        return self.position

    def get_direction(self):
        return self.direction

    def get_picture(self):
        return self.picture

    def get_max_distance(self):
        return self.max_distance

    def get_distance_traveled(self):
        return self.distance_traveled

    def get_damage(self):
        return self.damage

    def get_next_position(self):
        position_copied = self.position.copy()
        if self.direction == Direction.DOWN:
            position_copied[1] += 1
        elif self.direction == Direction.UP:
            position_copied[1] -= 1
        elif self.direction == Direction.RIGHT:
            position_copied[0] += 1
        else:
            position_copied[0] -= 1
        return position_copied

    def move_forward(self, distance):
        if self.direction == Direction.DOWN:
            self.position[1] += distance
        elif self.direction == Direction.UP:
            self.position[1] -= distance
        elif self.direction == Direction.RIGHT:
            self.position[0] += distance
        else:
            self.position[0] -= distance
        self.distance_traveled += 1

class Impact:
    def __init__(self, position, direction):
        self.position = position
        if direction == Direction.UP:
            self.picture = pygame.image.load("pictures/up_impact.png")
        elif direction == Direction.DOWN:
            self.picture = pygame.image.load("pictures/down_impact.png")
        elif direction == Direction.RIGHT:
            self.picture = pygame.image.load("pictures/right_impact.png")
        else:
            self.picture = pygame.image.load("pictures/left_impact.png")
        self.picture.set_colorkey(WHITE)
        self.iterarions = 2

    def get_picture(self):
        return self.picture

    def get_position(self):
        return self.position

    def get_iterations(self):
        return self.iterarions


class Direction:
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
