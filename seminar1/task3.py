# 1. Напишите программу, которая будет 
# на вход принимать число N и выводить числа от -N до N

# *Примеры:*

# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int(input('input the number: '))
# for i in range(-n, n+1):
#     print(i, end=' ')

N = int(input('input the number: '))
spam = list(range(-N, N+1))
print(spam)