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
    time.sleep(3)  # Задержка 3 секунды
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
else:
    print('Выбран неверный номер фигуры!')
