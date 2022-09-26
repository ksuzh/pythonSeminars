# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('input the number: '))


# def lst_fibonacci_num():
#     num = int(input('Введите любое натуральное число: '))
# fib = []
# a, b = 1, 1
# for i in range(num):
#     fib.append(a)
#     a, b = b, a + b
# a, b = 0, 1
# for j in range(num + 1):
#     fib.insert(0, a)
#     a, b = b, a - b
# print(f'Список чисел Фибоначчи для {num}: {fib}')


# lst_fibonacci_num()


fib = int(input('5# введите число for fib = '))
res_5 = []
for i in range(fib+1):
    if i==0:
        res_5.append(i)
    elif i==1:
        res_5.append(i)
        res_5.insert(0, i)
    else:
        res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
        res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
print(res_5)