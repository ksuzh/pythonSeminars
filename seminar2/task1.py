# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита О и Р. 
# Буква  О соответствует выпадению орла, буква Р - решки. Напишите программу, 
# которая подсчитывает наибольшее количество подряд выпавших решек. 

s=input()
t=0
while "Р"*(t+1) in s:
    t+=1
if t!=0:
    print(t)
else:
    print(0)