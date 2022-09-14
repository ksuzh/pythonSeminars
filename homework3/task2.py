# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

mylist = [int(i) for i in input().split()]
list_mult = []
for i in range ((len(mylist)+1) // 2):
    list_mult.append(mylist[i]*mylist[len(mylist)-1-i])
print(list_mult)