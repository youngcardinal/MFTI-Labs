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
if x == 1:
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
else:
    turtle.shape('turtle')
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    time.sleep(3)
