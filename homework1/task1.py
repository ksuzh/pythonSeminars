# Напишите программу, которая принимает 
# на вход цифру, обозначающую день недели, и 
# проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

wDay = int(input('input the number from 1 to 7: '))
if wDay == 6 or wDay ==7:
    print("It's a day off")
else:
    print("It's not")
