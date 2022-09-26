# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint
rand_list = []
n = int(input('input length of range: '))
for i in range(n):
    rand_list.append(randint(0, 20))

print(rand_list)
print(list(set(rand_list)))