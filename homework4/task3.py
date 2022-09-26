# Задайте последовательность чисел. 
# Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

from random import randint
rand_list = []
n = int(input('input length of range: '))
for i in range(n):
    rand_list.append(randint(0, 20))

print(rand_list)
print(list(set(rand_list)))