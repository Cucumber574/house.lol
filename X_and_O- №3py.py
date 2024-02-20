'''
+ поле из 9 клеток
+ игрок_1 - X
+ игрок_2 - 0
игроки ходят по очереди
начинает X
победа:
    3 одинаковых по горизонтали, вертикали или диагонали
ничья - нет свободны клеток и нет победителя
'''
EMPTY = '.'

from random import choice


def draw_filed(field: list) -> None:
    ''' Выводит на экран три ряда игрового поля '''
    for i in range(0, 7, 3):
        print(field[i], field[i + 1], field[i + 2])

def make_turt_robot(field: list, player: str, is_center: str, is_predicting:bool) -> None: 
    '''
     + собрать все возможгык свободные клетки
    сделать ход на случайную свободную клетку
    '''
    empty_cells_indexes = []
    for i in range(9):
        if field[i] == EMPTY:
            empty_cells_indexes.append(i)
        if is_center and 4 in empty_cells_indexes:
            field[4] = player
            return
        if is_predicting:
            for i in empty_cells_indexes:
                field[i] = player
                if get_winner(field, player):
                    return
                else:
                    field[i] = EMPTY
                    
        random = choice(empty_cells_indexes)
        field[random] = player

def make_turt_robot(field: list, player: str, is_center: str) -> None:
    '''
    Спрашивает номер клетки поля: 1-9 вкл
    Проверяет, есть ли на поле клетка с таким номером
    Проверяет, что клетка с этим номером свободна
    Если пройдет все проерки, ставит игрока в эту клетку
    '''
    while True:
        cell_num = int(input('Введите номер клетки (1-9): '))
        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер должен быть от 1 до 9 вкл.')
            continue
        if field[cell_num - 1] in players:
            print('Ошибка! Эта клетка занята.')
            continue
        field[cell_num - 1] = player
        break

def get_winner(field: list, player: str) -> str:
    #горизанталь
    for i in range(0, 7, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            return player

    #вертикаль   
    for i in range(3):
        if field[i] == field[i + 3] == field[i + 6] == player:
            return player

    #диоганаль  
    if field[i] == field[4] == field[8] == player:
        return player
    if field[i] == field[4] == field[6] == player:
        return player   
    return ''

def play_game(is_silent: bool) -> str:
player_1 = 'X'
player_2 = '0'
players = (player_1, player_2)
field = list(range(1, 10, 1))
moves = 1

while True:
    if moves > 9:
        if not is_silent:
            print('Ничья')
        return 'Ничья'
    if not is_silent:
        draw_filed(field)
    if moves % 2:
        player = player_1
        make_turt_robot(field, player, True, True)
    else:
        player = player_2
        make_turt_robot(field, player, False, True)
    moves += 1
    winner = get_winner(field, player)
    if winner:
        if not is_silent:
            draw_filed(field)
            print('Игра окончена, победил', winner)
        return winner

statistics = [0, 0, 0] #X, O, ничья
for i in range(1000):
    winner = play_game()
    if winner == 'X':
        statistics[0] +=1
    elif winner == '0':
        statistics[1] +=1
    else:
        statistics[2] +=1
print(statistics)