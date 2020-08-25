import pygame

WHITE = (255, 255, 255)


class Soldier:
    def __init__(self, matrix_position, picture, picture_selected, health, damage, shooting_distance, accuracy, moving_distance, exploring_range):
        self.position = matrix_position
        self.picture = pygame.image.load(picture)
        self.picture.set_colorkey(WHITE)
        self.picture_selected = pygame.image.load(picture_selected)
        self.heatlh = health
        self.damage = damage
        self.shooting_distance = shooting_distance
        self.accuracy = accuracy
        self.moving_distance = moving_distance
        self.exploring_range = exploring_range

    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    def get_picture_selected(self):
        return self.picture_selected

    def get_heatlh(self):
        return self.heatlh

    def get_damage(self):
        return self.damage

    def get_shooting_distance(self):
        return self.shooting_distance

    def get_accuracy(self):
        return self.accuracy

    def get_moving_distance(self):
        return self.moving_distance

    def get_exploring_range(self):
        return self.exploring_range

    def move(self, new_position):
        self.position = new_position

    def move_left(self, distance):
        self.position[0] -= distance

    def move_right(self, distance):
        self.position[0] += distance

    def move_up(self, distance):
        self.position[1] -= distance

    def move_down(self, distance):
        self.position[1] += distance

    def damage(self, damage):
        self.heatlh -= damage

    def heal(self, healing):
        self.heatlh += healing


class Infantry(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/soldier.png"
        PICTURE_SELECTED = "pictures/soldier_selected.png"
        HEALTH = 100
        DAMAGE = 20
        SHOOTING_DISTANCE = 5
        ACCURACY = 60
        MOVING_DISTANCE = 10
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MOVING_DISTANCE, EXPLORING_RANGE)


class Sniper(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/soldier.png"
        PICTURE_SELECTED = "pictures/soldier_selected.png"
        HEALTH = 80
        DAMAGE = 30
        SHOOTING_DISTANCE = 30
        ACCURACY = 80
        MOVING_DISTANCE = 5
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MOVING_DISTANCE, EXPLORING_RANGE)


class Gunner(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/soldier.png"
        PICTURE_SELECTED = "pictures/soldier_selected.png"
        HEALTH = 120
        DAMAGE = 40
        SHOOTING_DISTANCE = 10
        ACCURACY = 70
        MOVING_DISTANCE = 5
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MOVING_DISTANCE, EXPLORING_RANGE)


class Explorer(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/soldier.png"
        PICTURE_SELECTED = "pictures/soldier_selected.png"
        HEALTH = 80
        DAMAGE = 15
        SHOOTING_DISTANCE = 10
        ACCURACY = 60
        MOVING_DISTANCE = 10
        EXPLORING_RANGE = 15
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MOVING_DISTANCE, EXPLORING_RANGE)


class Enemy(Soldier):
    def __init__(self, position):
        PICTURE = "pictures/enemy.png"
        PICTURE_SELECTED = "pictures/enemy_selected.png"
        HEALTH = 100
        DAMAGE = 20
        SHOOTING_DISTANCE = 15
        ACCURACY = 60
        MOVING_DISTANCE = 10
        EXPLORING_RANGE = 5
        Soldier.__init__(self, position, PICTURE, PICTURE_SELECTED, HEALTH, DAMAGE, SHOOTING_DISTANCE, ACCURACY, MOVING_DISTANCE, EXPLORING_RANGE)