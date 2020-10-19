import math
import turtle
import time

print("Задача:\nНарисовать черепашкой выбранную фигуру\n"
      "Введите номер выбранной фигуры:\n"
      "1: Буква S\n"
      "2: Квадрат\n"
      "3: Круг\n"
      "4: Пирамида\n"
      "5: Звезда\n"
      "6: Спираль\n"
      "7: Квадратная 'спираль'\n"
      "8: Правильные многоугольники")
x = int(input())
if x == 1:              # Буква S
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    time.sleep(3)       # Задержка 3 секунды
elif x == 2:            # Квадрат
    turtle.shape('turtle')
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    time.sleep(3)
elif x == 3:            # Окружность
    turtle.shape('turtle')
    n = 360
    while n > 0:
        turtle.left(1)
        turtle.forward(1)
        n -= 1
    time.sleep(3)
elif x == 4:            # Пирамида
    turtle.shape('turtle')
    n = 15              # длина грани
    m = 1               # счетчик проходов
    while m <= 10:
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n)
        n += 30         # увеличиваем длину грани
        turtle.penup()
        turtle.forward(15)
        turtle.right(90)
        turtle.forward(15)
        turtle.right(180)
        turtle.pendown()
        m += 1          # увеличиваем счетчик на единицу
    time.sleep(3)
elif x == 5:            # Звезда
    print("Введите количество лучей звезды: ")
    m = int(input())
    n = 360/m           # Рассчитывается угол между лучами
    while m > 0:
        turtle.shape('turtle')
        turtle.forward(150)
        turtle.penup()
        turtle.backward(150)
        turtle.pendown()
        turtle.right(n)
        m -= 1
    time.sleep(3)
elif x == 6:            # Спираль
    from math import pi, sin, cos
    turtle.shape('turtle')
    for i in range(200):
        t = i / 10 * pi
        dx = t * cos(t)
        dy = t * sin(t)
        turtle.goto(dx, dy)
    time.sleep(3)
elif x == 7:             # Квадратная "спираль"
    turtle.shape('turtle')
    n = 10              # длина грани
    m = 1               # счетчик проходов
    while m <= 30:
        turtle.forward(n)
        turtle.left(90)
        n += 5          # увеличиваем величину грани
        m += 1          # увеличиваем счетчик на единицу
    time.sleep(3)
elif x == 8:            # Правильные многоугольники
    radius = 10
    side = 3

    def polygons(length_side, side):    # вводим функцию рисования многоугольника
        angle = 360 / side
        while side > 0:
            turtle.left(angle)
            turtle.forward(length_side)
            side -= 1
    while side < 13:
        length_side = 2 * radius * math.sin(math.pi / side)
        half_angle = (180 - 360 / side) / 2
        turtle.left(half_angle)

        polygons(length_side, side)
        turtle.right(half_angle)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
        side += 1
        radius += 10
else:
    print('Выбран неверный номер фигуры!')
