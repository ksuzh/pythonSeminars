# Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит пустая строка

fname = input('file ')
f = open(fname, 'w')
while True:
    s=input('word ')
    if s=='':
        break
f.write(s+'\n')
f.close()