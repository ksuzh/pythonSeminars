 # НОД

a = int(input('input the first number: '))
b = int(input('input the second number: '))

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)

if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)