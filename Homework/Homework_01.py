# Задача 1.
# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет


# print('Enter number from 1 to 7');
# day = int(input())

# if day < 1 or day > 7:
#     print('incorrect number!')

# elif day >= 1 and day <= 5:
#     print('No, this is not a weekend')

# else:
#     print('Yes, this is a weekend')


# Задача 2.
# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# x = int(input('Enter X: '))
# y = int(input('Enter Y: '))
# z = int(input('Enter Z: '))

# if not (x or y or z) == (not x) and (not y) and (not z):
#     print('True')
# else:
#     print('False')


# Задача 3.
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = float(input('Enter X: '))
# y = float(input('Enter Y: '))

# if x > 0 and y > 0:
#     print('quarter 1')
# elif x < 0 and y > 0:
#     print('quarter 2')
# elif x < 0 and y < 0:
#     print('quarter 3')
# elif x > 0 and y < 0:
#     print('quarter 4')
# elif x == 0 and y != 0:
#     print('dot is situated on Y axis')
# elif x != 0 and y == 0:
#     print('dot is situated on X axis')
# else:
#     print('dot is at the intersection of the coordinate axis (0;0)')


# Задача 4.
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# quart = int(input('Enter number of quarter: '))

# if quart < 1 or quart > 4:
#     print('incorrect number of quarter')
# elif quart == 1:
#     print('X ∈ (0; +∞); Y ∈ (0; +∞)')
# elif quart == 2:
#     print('X ∈ (-∞; 0); Y ∈ (0; +∞)')
# elif quart == 3:
#     print('X ∈ (-∞; 0); Y ∈ (-∞; 0)')
# else:
#     print('X ∈ (0; +∞); Y ∈ (-∞; 0)')


# 5- Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

x1 = float(input('Enter X coordinate of dot one: '))
y1 = float(input('Enter Y coordinate of dot one: '))

x2 = float(input('Enter X coordinate of dot two: '))
y2 = float(input('Enter Y coordinate of dot two: '))

distance = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
print(round(distance, 3))

