ho = int(input('Работа:\n0 - расшифровать\n1 - шифровать\n\n: '))

r = int(input('Алфавит ввода:\n0 - латинский\n1 - русский\n\n: '))
if r == 0: ALF = 'abcdefghijklmnopqrstuvwxyz'
else: ALF = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
n = int(input('число символов смещения: '))
if ho == 0: n = -n
    
S = str(input('текст: ').lower()) #ввод строки 

fr = str()

for i in S:
    if i.isalpha() != True: #пропуск не букв
        fr += i
        continue 
    fr += ALF[(ALF.index(i) + n) % len(ALF)] #шифрование-расшифрование
    
print('\nполучено: '+fr)
