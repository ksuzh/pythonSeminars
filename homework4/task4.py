# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# def create_polynomial():
#     try:
#         k = int(input('Введите натуральную степень: '))
#         a = int(random.randint(0, 100))
#         b = int(random.randint(0, 100))
#         c = int(random.randint(0, 100))
#     except ValueError:
#         print('Некорректный ввод')
#         print()
#         create_polynomial()
#     else:
#         if a != 0:
#             one = (str(a) + "x^" + str(k) + " + ")
#         else:
#             one = (str())

#     if b != 0:
#         two = (str(b) + "x" + " + ")
#     else:
#         two = (str())

#     if c != 0:
#         three = (str(c) + " = 0")
#     else:
#         three = (str())
#     print(f'{one}{two}{three}')


# create_polynomial()

import random
from random import randint

def create_polynomial(k):
    coefs = []
    for i in range(k+1):
        coefs.append(randint(-10, +10))
    return coefs

def format_polynomial(coefs):
    output = ""
    for i in range(k, -1, -1):
        c = coefs[i]
        if c != 0:
            if output != "": output += (" + " if c > 0 else " - ")
            else:
                if c < 0: output += "-"
            if c != 1 and c != -1:
                output += str(abs(c))
                if i > 0: output += "*"
            if i > 0: output += ("x" if i == 1 else "x^" + str(i))
    return output

k = int(input("Задайте степень k: "))
coefs = create_polynomial(k)
output = format_polynomial(coefs)
print(coefs)
print(output + " = 0")

with open ('polynomials.txt', 'w') as file:
    file.write(output)