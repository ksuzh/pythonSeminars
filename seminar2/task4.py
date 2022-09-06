# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

a = input('input something: ')
b = input('input something else: ')
if a > b:
    print(a.count(b))
elif b > a:
    print(b.count(a))

