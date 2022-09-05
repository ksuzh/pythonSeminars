# Напишите программу, которая принимает 
# на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('input x coordinate for the first point: '))
y1 = float(input('input y coordinate for the first point: '))
x2 = float(input('input x coordinate for the second point: '))
y2 = float(input('input y coordinate for the second point: '))

import math

length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
length = float('{:.2f}'.format(length))
print(length)

length = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(round(length, 2))
