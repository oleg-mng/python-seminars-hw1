# Задача 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
x=int(input('введите координату X отриц либо положит: '))
y=int(input('введите координату Y отриц либо положит: '))
if x>0 and y>0:
    print('вы ввели координаты 1-й четверти плоскости')
elif x<0 and y>0:
    print('вы ввели координаты 2-й четверти плоскости')
elif x<0 and y<0:
    print('вы ввели координаты 3-й четверти плоскости')
elif x>0 and y<0:
    print('вы ввели координаты 4-й четверти плоскости')