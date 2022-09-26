# В файле находится N натуральных чисел,
# записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

def find_num(lst):
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 1:
            return i, lst[i] - 1
    return -1, -1


with open("data.txt", "r") as fin:
    lst = [int(i) for i in fin.readline().split()]
    print(lst)
    pos, num = find_num(lst)
    print(pos, num)
    if (pos != -1):
        lst.insert(pos, num)
print(lst)
