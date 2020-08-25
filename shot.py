import pygame

WHITE = (255, 255, 255)


class Shot:
    def __init__(self, position, direction, max_distance, damage):
        if direction == Direction.DOWN or direction == Direction.UP:
            self.picture = pygame.image.load("pictures/vertical_shot.png")
        else:
            self.picture = pygame.image.load("pictures/horizontal_shot.png")
        self.direction = direction
        self.picture.set_colorkey(WHITE)
        self.position = position
        self.max_distance = max_distance
        self.distance_traveled = 0
        self.damage = damage

    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    def get_max_distance(self):
        return self.max_distance

    def get_distance_traveled(self):
        return self.distance_traveled

    def get_damage(self):
        return self.damage

    def move_forward(self, distance):
        if self.direction == Direction.DOWN:
            self.position[1] += distance
        elif self.direction == Direction.UP:
            self.position[1] -= distance
        elif self.direction == Direction.RIGHT:
            self.position[0] += distance
        else:
            self.position[0] -= distance


class Direction:
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
