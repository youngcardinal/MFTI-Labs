print("Задача:\nВывeдем на экран все целые числа из заданного диапзона [a, n)\nВведите число a:")
a = int(input())
print("Введите число n:")
n = int(input())
if a > n:
    for i in range(a, n):
        print(i)
else:
    print("Ошибка: не удалось построить диапазон, проверьте введеные значения, возможно a<=n !")
