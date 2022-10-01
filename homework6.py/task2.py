
# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = float(input('input the float number: '))

total = sum(map(int, filter(lambda i: i.isdigit(), str(num))))
print(total)