import pygame

WHITE = (255, 255, 255)

class Shot:
    def __init__(self, picture, position, max_distance, damage):
        self.picture = pygame.image.load(picture)
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
    
