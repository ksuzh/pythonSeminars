# Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('input the first number: '))
b = int(input('input the second number: '))

# def eucl(a,b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a        
#     print (a) 

def g_c_d(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2

print(g_c_d(a,b))

scm = a * b / g_c_d(a,b)
print(scm)