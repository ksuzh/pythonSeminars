# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

num = int(input('input the number: '))
factor_list = []
div = 2
while div <= num:
    if num % div == 0:
        factor_list.append(div)
        num /= div
    else:
        div +=1
print(factor_list)