# Задайте список. Напишите программу, 
# которая определит, присутствует ли 
# в заданном списке строк некое число.

mylist = ['2', 'qwe', 'hjjk', '345', '42']
num = input('input the number: ')
# for i in mylist:
#     if i == num:
#         print('yes')
#     else:
#         print('no')
    
if num in mylist: 
    print('yes')
else:
    print('no')