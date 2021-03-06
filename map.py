import pygame
import random
from soldiers import Infantry, Enemy, Gunner, Explorer, Sniper

WHITE = (255, 255, 255)
BACKGROUNG_COLOR = WHITE

MAP_WIDTH = 1200
MAP_HEIGTH = 600

rows = MAP_WIDTH // 20
columns = MAP_HEIGTH // 20
muro = pygame.image.load("pictures/muro.png")
muro.set_colorkey(WHITE)


class Map:
    def __init__(self):
        self.map_surface = pygame.Surface((MAP_WIDTH, MAP_HEIGTH))
        self.map_surface.fill(BACKGROUNG_COLOR)
        self.map = []  # Matriz de estado (1 Indica posicion ocupada o no accesible(muro o soldado))
        self.create_map()

    def create_map(self):
        # Inicializamos la matriz:
        for i in range(0, rows):
            self.map.append([0] * columns)

        # Generamos aleatoriamente el mapa:
        for i in range(0, rows):
            x = i * 20
            for j in range(0, columns):
                y = j * 20
                if i == 0 or i == rows - 1 or j == 0 or j == columns - 1 or random.randint(0, 100) >= 90:
                    self.map[i][j] = 1
                    self.map_surface.blit(muro, (x, y))

    def get_map_surface(self):
        return self.map_surface

    def get_map_matrix(self):
        return self.map

    def generate_soldiers(self, soldiers_list):
        # Generamos 4 soldados de infanteria, 2 francotiradores, 2 exploradores y 2 artilleros
        n = 0
        while n < 10:
            i = random.randint(1, rows // 4)
            j = random.randint(1, columns - 1)
            if self.map[i][j] == 0:  # Posicion libre:
                if n < 4:
                    soldier = Infantry([i, j])
                elif n < 6:
                    soldier = Gunner([i, j])
                elif n < 8:
                    soldier = Sniper([i, j])
                else:
                    soldier = Explorer([i, j])
                n += 1
                self.map[i][j] = 1
                soldiers_list.append(soldier)

    def generate_enemies(self, enemies_list):
        n = 0
        while n < 10:
            i = random.randint(rows - (rows // 4), rows - 1)
            j = random.randint(1, columns - 1)
            if self.map[i][j] == 0:  # Posicion libre:
                self.map[i][j] = 1
                n += 1
                enemy = Enemy([i, j])
                enemies_list.append(enemy)

    def get_soldier_selected(self, position, soldiers_list):
        i = position[0] // 20
        j = position[1] // 20
        if self.map[i][j] == 1:
            # Buscamos cual es el soldado seleccionado:
            for soldier in soldiers_list:
                if soldier.get_position()[0] == i and soldier.get_position()[1] == j:
                    return soldier
            return None

    # Devuelve el estado (valor) de la posicion indicada
    def get_state_position(self, position):
        return self.map[position[0]][position[1]]

    # Modifica el estado (valor) de la posicion indicada
    def set_state_position(self, position, value):
        self.map[position[0]][position[1]] = value
