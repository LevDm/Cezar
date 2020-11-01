import logging


def sapros(ogranbas,watt,par_1,par_2): #фунция запроса и проверки значения ответа 
    go = True
    
    while go == True:
        ye = 0     
        bas = [1,0]
        if ogranbas == True: print('----------\n'+watt+':\n0 - '+par_1+'\n1 - '+par_2)
        else: print('----------\n'+watt)
        vosvrat = input(':')
        if  vosvrat.isdigit() == True:
            vosvrat = int(vosvrat)
            go = False
        else:
            go = True
            print('необходимо целое число')
            logger.info("Пользователь ошибся вводом значения")
        if ogranbas != True: continue
        for i in bas:
            if vosvrat == i: ye +=1 
        if ye == 1: go = False 
        else:
            print('Введеное значение не совпадает с возможными')
            logger.info("Пользователь ошибся вводом значения")
            go = True
    return vosvrat 


# Настройка логгера
logger = logging.getLogger("Cezar")
logger.setLevel(logging.INFO)


# создание log-файла
fh = logging.FileHandler("cezar's.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


cezar = True
while cezar == True: #основной цикл запросов программы
    logger.info("Программа запущена")
    
    ho = sapros(True,'Режим работы','расшифровать','шифровать')
    logger.info("Пользователь выбрал действие %s" %ho )


    r = sapros(True,'Алфавит ввода','латинский','русский')
    logger.info("Пользователь выбрал действие %s" %r )
    
    if r == 0: ALF = 'abcdefghijklmnopqrstuvwxyz'
    else: ALF = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    n = sapros(False,'Число символов смещения','','')
    logger.info("Пользователь выбрал шаг %s" %n )
    
    if ho == 0: n = -n

    go = True
    while go == True:
        print('----------\nЦифры, знаки препинания и специальные символы не шифруются!')
        S = str(input('текст: ').lower()) #ввод строки
        logger.info("Пользователь выбрал ввел строку %s" %S )
        for i in S:
            if i.isalpha() != True: continue
            if ALF.count(i) != 0:
                go = False
                continue
            else:
                print('символы не соответствуют выбранному алфавиту')
                logger.info("Пользователь ошибся алфавитом")
                go = True
                break
            
    fr = str()
    for i in S:
        if i.isalpha() != True:
            fr += i
            continue 
        fr += ALF[(ALF.index(i) + n) % len(ALF)] #шифрование-расшифрование
    
    print('\nполучено: '+fr)
    
    progon = sapros(True,'Ещё разок?','да','нет')
    logger.info("Пользователь выбрал действие %s" %progon )
    if progon == 1: cezar = False
    
logger.info("Программа остановлена")
