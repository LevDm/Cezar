r = int(input('Алфавит ввода:\n0 - латинский\n1 - русский\n\n:'))
if r == 0: ALF = ' abcdefghijklmnopqrstuvwxyz'
else: ALF = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
n = int(input('число символов смещения:'))
S = str(input('текст:').lower()) #ввод строки 

fr = str()
for i in S:
    fr += ALF[(ALF.index(i) + n) % len(ALF)] #шифрование
    
for i in range(len(S)): #пробелы
    if S[i] == ' ':
        fr = fr.replace(fr[i],' ')
    
print('\nполучено:'+fr)
