import pygame
from shot import Direction

WHITE = (255, 255, 255)


class Soldier:
    def __init__(self, matrix_position, picture, picture_selected, health, damage, shooting_distance, accuracy, max_moving_distance, exploring_range):
        self.position = matrix_position
        self.picture = pygame.image.load(picture)
        self.picture.set_colorkey(WHITE)
        self.picture_selected = pygame.image.load(picture_selected)
        self.health = health
        self.damage = damage
        self.shooting_distance = shooting_distance
        self.accuracy = accuracy
        self.max_moving_distance = max_moving_distance
        self.distance_traveled = 0
        self.exploring_range = exploring_range

    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    def get_picture_selected(self):
        return self.picture_selected

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_shooting_distance(self):
        return self.shooting_distance

    def get_accuracy(self):
        return self.accuracy

    def get_max_moving_distance(self):
        return self.max_moving_distance

    def get_distance_traveled(self):
        return self.distance_traveled

    def reset_distance_traveled(self):
        self.distance_traveled = 0

    def get_exploring_range(self):
        return self.exploring_range

    def get_next_position(self, direction):
        position_copied = self.position.copy()
        if direction == Direction.DOWN:
            position_copied[1] += 1
        elif direction == Direction.UP:
            position_copied[1] -= 1
        elif direction == Direction.RIGHT:
            position_copied[0] += 1
        else:
            position_copied[0] -= 1
        return position_copied

    def move(self, distance, direction):
        if direction == Direction.DOWN:
            self.position[1] += distance
        elif direction == Direction.UP:
            self.position[1] -= distance
        elif direction == Direction.RIGHT:
            self.position[0] += distance
        else:
            self.position[0] -= distance
        self.distance_traveled += distance

    def set_damage(self, damage):
        self.health -= damage

    def set_healing(self, healing):
        self.health += healing


class Infantry(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/infantry.png"
        PICTURE_SELECTED = "pictures/infantry_selected.png"
        HEALTH = 100
        DAMAGE = 60
        SHOOTING_DISTANCE = 5
        ACCURACY = 60
        MAX_MOVING_DISTANCE = 10
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MAX_MOVING_DISTANCE, EXPLORING_RANGE)


class Sniper(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/sniper.png"
        PICTURE_SELECTED = "pictures/sniper_selected.png"
        HEALTH = 80
        DAMAGE = 100
        SHOOTING_DISTANCE = 30
        ACCURACY = 80
        MAX_MOVING_DISTANCE = 5
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MAX_MOVING_DISTANCE, EXPLORING_RANGE)


class Gunner(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/gunner.png"
        PICTURE_SELECTED = "pictures/gunner_selected.png"
        HEALTH = 120
        DAMAGE = 80
        SHOOTING_DISTANCE = 10
        ACCURACY = 70
        MAX_MOVING_DISTANCE = 5
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MAX_MOVING_DISTANCE, EXPLORING_RANGE)


class Explorer(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/explorer.png"
        PICTURE_SELECTED = "pictures/explorer_selected.png"
        HEALTH = 80
        DAMAGE = 40
        SHOOTING_DISTANCE = 10
        ACCURACY = 60
        MAX_MOVING_DISTANCE = 10
        EXPLORING_RANGE = 15
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MAX_MOVING_DISTANCE, EXPLORING_RANGE)


class Enemy(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/enemy.png"
        PICTURE_SELECTED = "pictures/enemy_selected.png"
        HEALTH = 100
        DAMAGE = 60
        SHOOTING_DISTANCE = 5
        ACCURACY = 60
        MAX_MOVING_DISTANCE = 10
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MAX_MOVING_DISTANCE, EXPLORING_RANGE)