# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = input('input the number: ')
list_num = [int(el) for el in num if el.isdigit()]
print(list_num)
total = 0
for number in list_num:
    total += number
print(total)