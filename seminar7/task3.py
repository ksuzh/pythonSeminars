# Напишите функцию triangle(a, b, c), 
# которая принимает на вход три длины отрезков и определяет, 
# можно ли из этих отрезков составить треугольник.
# Входные данные
# Выходные данные
# triangle(1, 1, 2)
# Это не треугольник
# triangle(7, 6, 10)

# Это треугольник

def triangle(x, y, z):
    return x+y>z and x+z>y and y+z>x

a = 7
b = 6
c = 10
if triangle(a, b, c):
    print('its triangle')
else:
    print('its not')
    