# Напишите программу, которая по заданному 
# номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

num = int(input('input the number from 1 to 4: '))
if num == 1:
    print('x > 0 and y > 0')
elif num == 2:
    print('x < 0 and y > 0')
elif num == 3:
    print('x < 0 and y < 0')
elif num == 4:
    print('x > 0 and y < 0')
else:
    print('number should be from 1 to 4!')