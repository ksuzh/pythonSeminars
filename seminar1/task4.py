# 2. Напишите программу, которая будет принимать 
# на вход дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

number = float(input('input the number: '))
num = int((number * 10) % 10)
if num == 0:
    print('no digit')
else:
    print(num)
