import pygame
import sys
from soldiers import Infantry, Enemy
from shot import Shot, Direction
from map import Map

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKGROUNG_COLOR = WHITE
SCREEN_WIDTH = 1200
SCREEN_HEIGTH = 650


soldiers = []
enemies = []
shots = []

def move_left(soldier):
    map_matrix = map.get_map_matrix()
    if map_matrix[soldier.get_position()[0] - 1][soldier.get_position()[1]] == 0:
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 0
        soldier.move_left(1)
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 1


def move_right(soldier):
    map_matrix = map.get_map_matrix()
    if map_matrix[soldier.get_position()[0] + 1][soldier.get_position()[1]] == 0:
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 0
        soldier.move_right(1)
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 1


def move_up(soldier):
    map_matrix = map.get_map_matrix()
    if map_matrix[soldier.get_position()[0]][soldier.get_position()[1] - 1] == 0:
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 0
        soldier.move_up(1)
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 1


def move_down(soldier):
    map_matrix = map.get_map_matrix()
    if map_matrix[soldier.get_position()[0]][soldier.get_position()[1] + 1] == 0:
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 0
        soldier.move_down(1)
        map_matrix[soldier.get_position()[0]][soldier.get_position()[1]] = 1

def shot_right(soldier):
    # TODO: Comprobar que el disparo sea certero! (accuracy)
    shot_position = soldier.get_position().copy()
    shot = Shot(shot_position, Direction.RIGHT, soldier.get_shooting_distance(), soldier.get_damage())
    shots.append(shot)

def shot_left(soldier):
    shot_position = soldier.get_position().copy()
    shot = Shot(shot_position, Direction.LEFT, soldier.get_shooting_distance(), soldier.get_damage())
    shots.append(shot)

def shot_up(soldier):
    shot_position = soldier.get_position().copy()
    shot = Shot(shot_position, Direction.UP, soldier.get_shooting_distance(), soldier.get_damage())
    shots.append(shot)

def shot_down(soldier):
    shot_position = soldier.get_position().copy()
    shot = Shot(shot_position, Direction.DOWN, soldier.get_shooting_distance(), soldier.get_damage())
    shots.append(shot)

def run_game():

    clock = pygame.time.Clock()
    game_over = False

    selected_soldier = None

    while not game_over:
        # Control de fps:
        clock.tick(15)
        screen.blit(map_surface, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                selected_soldier = map.get_soldier_selected(position, soldiers)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and selected_soldier is not None:
                    move_left(selected_soldier)
                elif event.key == pygame.K_RIGHT and selected_soldier is not None:
                    move_right(selected_soldier)
                elif event.key == pygame.K_UP and selected_soldier is not None:
                    move_up(selected_soldier)
                elif event.key == pygame.K_DOWN and selected_soldier is not None:
                    move_down(selected_soldier)
                elif event.key == pygame.K_SPACE and selected_soldier is not None:
                    print(map)
                elif event.key == pygame.K_w and selected_soldier is not None:
                    shot_up(selected_soldier)
                elif event.key == pygame.K_a and selected_soldier is not None:
                    shot_left(selected_soldier)
                elif event.key == pygame.K_d and selected_soldier is not None:
                    shot_right(selected_soldier)
                elif event.key == pygame.K_s and selected_soldier is not None:
                    shot_down(selected_soldier)

        # Dibujamos los jugadores y los enemigos
        for soldier in soldiers:
            if selected_soldier is not None and selected_soldier == soldier:
                screen.blit(soldier.get_picture_selected(), (soldier.get_position()[0] * 20, soldier.get_position()[1] * 20))
            screen.blit(soldier.get_picture(), (soldier.get_position()[0] * 20, soldier.get_position()[1] * 20))

        for enemy in enemies:

            screen.blit(enemy.get_picture(), (enemy.get_position()[0] * 20, enemy.get_position()[1] * 20))

        for shot in shots:
            shot.move_forward(1)
            screen.blit(shot.get_picture(), (shot.get_position()[0] * 20, shot.get_position()[1] * 20))

        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
map = Map()
map.generate_soldiers(soldiers)
map.generate_enemies(enemies)
map_surface = map.get_map_surface()
run_game()