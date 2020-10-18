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
      "7: Квадратная спираль\n"
      "8: Звезда Давида")
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
else:
    print('Выбран неверный номер фигуры!')
