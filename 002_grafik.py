# Каскадные условные функции:
# по данным ненулевым числам x и y определяет,
# в какой из четвертей координатной плоскости находится точка (x,y)
print("Задача:\nОпределить какой четверти принадлежит точка с введенными координатами\nВведите число x:")
x = int(input())
print("Введите число y:")
y = int(input())
if x > 0 and y > 0:
    print('Первая четверть графика')
elif y < 0:
    print('Четвертая четверть графика')
elif y > 0:
    print('Вторая четверть графика')
else:
    print('Третья четверть графика')
