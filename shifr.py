ho = int(input('Работа:\n0 - расшифровать\n1 - шифровать\n\n: '))

r = int(input('Алфавит ввода:\n0 - латинский\n1 - русский\n\n: '))
if r == 0: ALF = 'abcdefghijklmnopqrstuvwxyz'
else: ALF = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    
n = int(input('число символов смещения: '))
if ho == 0: n = -n
    
go = True
while go == True: #Ввод строки с проверкой выбраного алфавита
    S = str(input('текст: ').lower())
    for i in S:
        if i.isalpha() != True: continue
        if ALF.count(i) != 0:
            go = False
            continue
        else:
            print('символы не соответствуют единому выбранному алфавиту')
            go = True
            break
            

fr = str()

for i in S:
    if i.isalpha() != True: #пропуск не букв
        fr += i
        continue 
    fr += ALF[(ALF.index(i) + n) % len(ALF)] #шифрование-расшифрование
    
print('\nполучено: '+fr)
