# 3. Напишите программу, которая принимает 
# на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

number = int(input('input the number: '))

if (number % 10 ==0 or number % 15 ==0) and number % 30 != 0:
    print('thats what we looking for!')
else:
    print('doesnt fit') 