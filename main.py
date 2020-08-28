import pygame
import sys
from shot import Shot, Direction, Impact
from map import Map

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKGROUNG_COLOR = WHITE
SCREEN_WIDTH = 1200
SCREEN_HEIGTH = 650
PICTURES_SIZE = 20

players = []
enemies = []
shots = []
impacts = []
turn_enemy = False


def move(soldier, direction):
    distance_traveled = soldier.get_distance_traveled()
    max_distance = soldier.get_max_moving_distance()
    next_position = soldier.get_next_position(direction)
    if map.get_state_position(next_position) == 0 and distance_traveled < max_distance:
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
    # A parte de cambiar el turno reestablecemos la distancia recorrida de los jugadores y enemigos:
    global turn_enemy
    if turn_enemy:
        for enemy in enemies:
            enemy.reset_distance_traveled()
        turn_enemy = False
    else:
        for player in players:
            player.reset_distance_traveled()
        turn_enemy = True


def enemy_turn():
    for enemy in enemies:
        for n in range (0, enemy.get_max_moving_distance()):
            nearest_soldier = get_nearest_player(enemy.get_position(), players)
            if nearest_soldier is not None:
                moving_direction = get_direction(enemy, nearest_soldier)
                if in_range(enemy, nearest_soldier):
                    shot_direction = get_shot_direction(enemy, nearest_soldier)
                    create_shot(enemy, shot_direction)
                else:
                    move(enemy, moving_direction)
    change_turn()


def get_nearest_player(position, players_list):
    nearest = None
    nearest_distance = 200
    for soldier in players_list:
        distance = abs(position[0] - soldier.get_position()[0]) + abs(position[1] - soldier.get_position()[1])
        if distance < nearest_distance:
            nearest = soldier
            nearest_distance = distance
    return nearest


def in_range(from_soldier, to_soldier):
    n = from_soldier.get_shooting_distance()
    if (from_soldier.get_position()[0] - to_soldier.get_position()[0] in range(-n, n)
        and from_soldier.get_position()[1] - to_soldier.get_position()[1] == 0) \
            or (from_soldier.get_position()[0] - to_soldier.get_position()[0] == 0
                and from_soldier.get_position()[1] - to_soldier.get_position()[1] in range(-n, n)):
        return True
    return False


def get_shot_direction(from_soldier, to_soldier):
    if from_soldier.get_position()[0] - to_soldier.get_position()[0] < 0 \
            and from_soldier.get_position()[1] == to_soldier.get_position()[1]:
        return Direction.RIGHT
    elif from_soldier.get_position()[0] - to_soldier.get_position()[0] > 0 \
            and from_soldier.get_position()[1] == to_soldier.get_position()[1]:
        return Direction.LEFT
    elif from_soldier.get_position()[1] - to_soldier.get_position()[1] < 0 \
            and from_soldier.get_position()[0] == to_soldier.get_position()[0]:
        return Direction.DOWN
    elif from_soldier.get_position()[1] - to_soldier.get_position()[1] > 0 \
            and from_soldier.get_position()[0] == to_soldier.get_position()[0]:
        return Direction.UP
    else:
        return None


def get_direction(from_soldier, to_soldier):
    # TODO: mejorar este metodo
    if from_soldier.get_position()[0] - to_soldier.get_position()[0] < 0 \
            and map.get_state_position(from_soldier.get_next_position(Direction.RIGHT)) == 0:
        return Direction.RIGHT
    elif from_soldier.get_position()[0] - to_soldier.get_position()[0] > 0 \
            and map.get_state_position(from_soldier.get_next_position(Direction.LEFT)) == 0:
        return Direction.LEFT
    elif from_soldier.get_position()[1] - to_soldier.get_position()[1] <= 0 \
            and map.get_state_position(from_soldier.get_next_position(Direction.DOWN)) == 0:
        return Direction.DOWN
    elif from_soldier.get_position()[1] - to_soldier.get_position()[1] >= 0 \
            and map.get_state_position(from_soldier.get_next_position(Direction.UP)) == 0:
        return Direction.UP


def end_menu(player_is_winner):
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_over()

        if player_is_winner:
            fuente_game_over = pygame.font.Font(None, 100)
            text_game_over = "YOU WIN"
            text_game_over = fuente_game_over.render(text_game_over, 0, RED)
        else:
            fuente_game_over = pygame.font.Font(None, 100)
            text_game_over = "YOU LOOSE"
            text_game_over = fuente_game_over.render(text_game_over, 0, RED)

        fuente_play_again = pygame.font.Font(None, 30)
        text_play_again = "Press space to play again"
        text_play_again = fuente_play_again.render(text_play_again, 0, WHITE)
        screen.blit(text_game_over, (100, 200))
        screen.blit(text_play_again, (200, 400))
        pygame.display.update()


def start_over():
    # TODO: Resolver problemas
    shots.clear()
    enemies.clear()
    players.clear()
    impacts.clear()
    map = Map()
    map.generate_soldiers(players)
    map.generate_enemies(enemies)
    map_surface = map.get_map_surface()
    run_game()


def run_game():


    global turn_enemy
    game_over = False

    selected_soldier = None

    while not game_over:
        # Control de fps:
        clock.tick(15)
        screen.blit(map_surface, (0, 0))
        if turn_enemy:
            enemy_turn()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    selected_soldier = map.get_soldier_selected(position, players)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and selected_soldier is not None:
                        move(selected_soldier, Direction.LEFT)
                    elif event.key == pygame.K_RIGHT and selected_soldier is not None:
                        move(selected_soldier, Direction.RIGHT)
                    elif event.key == pygame.K_UP and selected_soldier is not None:
                        move(selected_soldier, Direction.UP)
                    elif event.key == pygame.K_DOWN and selected_soldier is not None:
                        move(selected_soldier, Direction.DOWN)
                    elif event.key == pygame.K_SPACE:
                        selected_soldier = None
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
        for player in players:
            if player.get_health() <= 0:
                map.set_state_position(player.get_position(), 0)
                players.remove(player)
            elif selected_soldier is not None and selected_soldier == player:
                screen.blit(player.get_picture_selected(), (player.get_position()[0] * PICTURES_SIZE, player.get_position()[1] * PICTURES_SIZE))
            else:
                screen.blit(player.get_picture(), (player.get_position()[0] * PICTURES_SIZE, player.get_position()[1] * PICTURES_SIZE))

        for enemy in enemies:
            if enemy.get_health() <= 0:
                map.set_state_position(enemy.get_position(), 0)
                enemies.remove(enemy)
            else:
                screen.blit(enemy.get_picture(), (enemy.get_position()[0] * PICTURES_SIZE, enemy.get_position()[1] * PICTURES_SIZE))

        for shot in shots:
            # Caso 1: El disparo no ha alcanzado su maxima distancia y no ha chocado con nada
            if shot.get_max_distance() > shot.get_distance_traveled() and map.get_state_position(shot.get_next_position()) == 0:
                shot.move_forward(1)
                screen.blit(shot.get_picture(), (shot.get_position()[0] * PICTURES_SIZE, shot.get_position()[1] * PICTURES_SIZE))
            # Caso 2: El disparo choca con algo (muro o enemigo)
            elif map.get_state_position(shot.get_next_position()) == 1:
                for enemy in enemies:
                    if contact(shot, enemy):
                        enemy.set_damage(shot.get_damage())
                for player in players:
                    if contact(shot, player):
                        player.set_damage(shot.get_damage())
                create_impact(shot.get_position(), shot.get_direction())
                shots.remove(shot)
            # Caso 3: El disparo ha alcanzao su maxima distancia
            else:
                shots.remove(shot)

        if len(enemies) == 0:
            end_menu(True)
            game_over = True

        elif len(players) == 0:
            end_menu(False)
            game_over = True

        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
clock = pygame.time.Clock()
map = Map()
map.generate_soldiers(players)
map.generate_enemies(enemies)
map_surface = map.get_map_surface()
run_game()