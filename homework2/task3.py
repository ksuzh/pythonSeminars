# Задайте список из n чисел последовательности (1+1/n)^n и 
# выведите на экран их сумму.

n = int(input('input the number: '))
a = []
for i in range(1, n + 1):
    i = round((1 + 1 / i)**i, 2)
    a.append(i)
print(a)

print(round(sum(a),2))

