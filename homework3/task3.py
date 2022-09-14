# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

mylist = [1.1, 1.2, 3.1, 5, 10.01]
list_float = []
for i in range(len(mylist)):
    if mylist[i] - int(mylist[i]) != 0:
        list_float.append(round(mylist[i] - int(mylist[i]), 2))
print(list_float)

print(max(list_float)-min(list_float))