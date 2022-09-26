#  Задайте строку из набора чисел. 
#  Напишите программу, которая покажет большее и меньшее число. 
#  В качестве символа-разделителя используйте пробел.

num_list = input('input the numbers, use space to split: '). split()
print(num_list)

int_list = list(map(int, num_list))

print(max(int_list))
print(min(int_list))

# str = '12 32 0 15'
# lst = [int(i) for i in str.split()]
# print(min(lst))
# print(max(lst))