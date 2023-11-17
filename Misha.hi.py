import turtle
from random import randint


turtle.speed(8)
turtle.colormode(255)

def draw_house(
    x=0,
    y=0,
    base_w=100,
    base_h=10,
    base_color='grey',
    walls_w=100,
    walls_h=60,
    walls_color='red',
    roof_w=100,
    roof_h=30,
    roof_color='black'
):
    '''
    вызывает функцию рисования фундамента
    вызывает функцию рисования стен
    вызывает функцию рисования крыши

    x - левый нижний угол фундамента
    y - левый нижний угол фундамента

    base_w - ширина фундамента
    base_h - высота фундамента
    base_color - цвет фундамента

    walls_w - ширина стен
    walls_h - высота стен
    walls_color - цвет стен

    roof_w - ширина крыши
    roof_h - высота крыши
    roof_color - цвет крыши
    '''

    print('начинаем строить дом')
    draw_base(x, y, base_w, base_h, base_color)
    draw_walls(x, y, walls_w, walls_h, walls_color, base_h)
    draw_roof(x, y, roof_w, roof_h, roof_color, base_h, walls_h, walls_w, roof_w, roof_color)


def draw_base(x, y, width, height, color):
    ''' рисует фундамент '''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_walls(x, y, width, height, color, base_height):
    ''' рисует стены '''
    turtle.penup()
    turtle.goto(x, y + base_height)
    turtle.pendown()
    draw_rectangle(width, height, color)


def draw_roof(x, y, width, height, color, base_h, wall_h, wall_w, roof_w, roof_color):
    ''' рисует крышу '''
    turtle.penup()
    roof_y = y + base_h + wall_h 
    turtle.goto(x, y + base_h + wall_h)
    turtle.pendown()
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    turtle.forward(wall_w // 2 + width // 2)
    turtle.goto(x + wall_w // 2, roof_y + height)
    turtle.goto(x - wall_w // 2, roof_y)
    turtle.goto(x, y + base_h + wall_h)
    turtle.end_fill()


def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()


def draw_street(x, y, houses):
    counter = 0
    while counter <= houses:
        base_w = randint(30,70)
        base_h = base_w * 0.1
        base_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        walls_w = randint(int(base_w * 0.9), base_w)
        walls_h = randint(walls_w, walls_w * 2)
        walls_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        roof_w = randint(walls_w, int(walls_w * 1.2))
        roof_h = randint(roof_w, int(roof_w * 1.5))
        roof_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        draw_house(x=x, y=y, base_w=base_w, walls_w=walls_w, roof_w=roof_w, base_color=base_color, base_h=base_h, walls_h=walls_h, walls_color=walls_color, roof_color=roof_color)
        counter += 1
        x += roof_w + base_w

draw_street(-200, 0, 5)

turtle.done()
