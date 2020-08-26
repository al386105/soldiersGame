import pygame
import sys
from shot import Shot, Direction, Impact
from map import Map
import random

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKGROUNG_COLOR = WHITE
SCREEN_WIDTH = 1200
SCREEN_HEIGTH = 650
PICTURES_SIZE = 20

soldiers = []
enemies = []
shots = []
impacts = []
turn_enemy = False


def move(soldier, direction):
    next_position = soldier.get_next_position(direction)
    if map.get_state_position(next_position) == 0:
        map.set_state_position(soldier.get_position(), 0)
        soldier.move(1, direction)
        map.set_state_position(next_position, 1)


def contact(shot, enemy):
    if shot.get_next_position() == enemy.get_position():
        return True
    else:
        return False


def create_shot(soldier, direction):
    shot_position = soldier.get_position().copy()
    shot = Shot(shot_position, direction, soldier.get_shooting_distance(), soldier.get_damage())
    shots.append(shot)


def create_impact(position, direction):
    impact = Impact(position, direction)
    screen.blit(impact.get_picture(),
                (impact.get_position()[0] * PICTURES_SIZE, impact.get_position()[1] * PICTURES_SIZE))


def change_turn():
    global turn_enemy
    if turn_enemy:
        turn_enemy = False
    else:
        turn_enemy = True


def enemy_move():
    for enemy in enemies:
        for i in range(0, enemy.get_max_moving_distance()):
            nearest_soldier = get_nearest_soldier(enemy.get_position(), soldiers)
            if nearest_soldier is not None:
                direction = get_direction(enemy, nearest_soldier)
                if in_range(enemy, nearest_soldier):
                    create_shot(enemy, direction)
                else:
                    move(enemy, direction)
            else:
                print("F")

    change_turn()


def get_nearest_soldier(position, soldiers_list):
    nearest = None
    nearest_distance = 200
    for soldier in soldiers_list:
        distance = abs(position[0] - soldier.get_position()[0]) + abs(position[1] - soldier.get_position()[1])
        if distance < nearest_distance:
            nearest = soldier
            nearest_distance = distance
    return nearest


def in_range(enemy, soldier):
    n = enemy.get_shooting_distance()
    if (enemy.get_position()[0] - soldier.get_position()[0] in range(-n, n)
            and enemy.get_position()[1] - soldier.get_position()[1] == 0) \
            or (enemy.get_position()[0] - soldier.get_position()[0] == 0
            and enemy.get_position()[1] - soldier.get_position()[1] in range(-n, n)):
        return True
    return False


def get_direction(enemy, soldier):
    # TODO: mejorar este metodo
    if enemy.get_position()[0] - soldier.get_position()[0] < 0 \
            and map.get_state_position(enemy.get_next_position(Direction.RIGHT)) == 0:
        return Direction.RIGHT
    elif enemy.get_position()[0] - soldier.get_position()[0] > 0 \
            and map.get_state_position(enemy.get_next_position(Direction.LEFT)) == 0:
        return Direction.LEFT
    elif enemy.get_position()[1] - soldier.get_position()[1] < 0 \
            and map.get_state_position(enemy.get_next_position(Direction.DOWN)) == 0:
        return Direction.DOWN
    elif enemy.get_position()[1] - soldier.get_position()[1] > 0 \
            and map.get_state_position(enemy.get_next_position(Direction.UP)) == 0:
        return Direction.UP


def run_game():

    global turn_enemy
    game_over = False

    selected_soldier = None

    while not game_over:
        # Control de fps:
        clock.tick(10)
        screen.blit(map_surface, (0, 0))
        if turn_enemy:
            enemy_move()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    selected_soldier = map.get_soldier_selected(position, soldiers)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and selected_soldier is not None:
                        move(selected_soldier, Direction.LEFT)
                    elif event.key == pygame.K_RIGHT and selected_soldier is not None:
                        move(selected_soldier, Direction.RIGHT)
                    elif event.key == pygame.K_UP and selected_soldier is not None:
                        move(selected_soldier, Direction.UP)
                    elif event.key == pygame.K_DOWN and selected_soldier is not None:
                        move(selected_soldier, Direction.DOWN)
                    elif event.key == pygame.K_SPACE and selected_soldier is not None:
                        change_turn()
                    elif event.key == pygame.K_w and selected_soldier is not None:
                        create_shot(selected_soldier, Direction.UP)
                    elif event.key == pygame.K_a and selected_soldier is not None:
                        create_shot(selected_soldier, Direction.LEFT)
                    elif event.key == pygame.K_d and selected_soldier is not None:
                        create_shot(selected_soldier, Direction.RIGHT)
                    elif event.key == pygame.K_s and selected_soldier is not None:
                        create_shot(selected_soldier, Direction.DOWN)

        # Dibujamos los jugadores y los enemigos
        for soldier in soldiers:
            if selected_soldier is not None and selected_soldier == soldier:
                screen.blit(soldier.get_picture_selected(), (soldier.get_position()[0] * PICTURES_SIZE, soldier.get_position()[1] * PICTURES_SIZE))
            screen.blit(soldier.get_picture(), (soldier.get_position()[0] * PICTURES_SIZE, soldier.get_position()[1] * PICTURES_SIZE))

        for enemy in enemies:
            screen.blit(enemy.get_picture(), (enemy.get_position()[0] * PICTURES_SIZE, enemy.get_position()[1] * PICTURES_SIZE))

        for shot in shots:
            # Caso 1: El disparo no ha alcanzado su maxima distancia y no ha chocado con nada
            if shot.get_max_distance() > shot.get_distance_traveled() and map.get_state_position(shot.get_next_position()) == 0:
                shot.move_forward(1)
                screen.blit(shot.get_picture(), (shot.get_position()[0] * PICTURES_SIZE, shot.get_position()[1] * PICTURES_SIZE))
            # Caso 2: El disparo choca con algo (muro o enemigo) Aqui comprobamos que el disparo es certero.

            elif map.get_state_position(shot.get_next_position()) == 1:
                for enemy in enemies:
                    if contact(shot, enemy) and random.randint(0, 100) <= selected_soldier.get_accuracy():
                        map.set_state_position(enemy.get_position(), 0)
                        enemies.remove(enemy)
                create_impact(shot.get_position(), shot.get_direction())
                shots.remove(shot)
            # Caso 3: El disparo ha alcanzao su maxima distancia
            else:
                shots.remove(shot)
        if len(enemies) == 0:
            #TODO: llamar a metodo victory
            game_over = True

        elif len(soldiers) == 0:
            #TODO: llamar al metodo defeated
            game_over = True
        

        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
clock = pygame.time.Clock()
map = Map()
map.generate_soldiers(soldiers)
map.generate_enemies(enemies)
map_surface = map.get_map_surface()
run_game()