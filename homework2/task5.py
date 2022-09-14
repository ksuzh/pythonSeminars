# Реализуйте алгоритм перемешивания списка.

import random

# mylist = [(i) for i in input().split()]
# print(mylist)

# random.shuffle(mylist)
# print(mylist)


# list = ["Anna", "Alex", 3.14159, 0]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     temp = list[i]
#     list[i] = list[index_a]
#     list[index_a] = temp
# print(list)


list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a] = list[index_a], list[i]    
print(list)