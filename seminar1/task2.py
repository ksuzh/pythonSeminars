# 2. Напишите программу, которая на вход 
# принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

numbers = [1, 4, 8, 7, 5]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)

# numbers = [int(i) for i in input().split()]
# # numbers = list(map(int, input().split()[:5]))  
# max = numbers[0]
# for i in range(len(numbers)):
#     if numbers[i] > max:
#         max = numbers[i]
# print(max)


# numbers = [int(i) for i in input().split()[:5]]
# or numbers = list(map(int,  input().split()[:n]))