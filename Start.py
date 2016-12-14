def Decode_file(file_name):
    '''Принимает на вход имя исходного файла, возвращает строку с раскодированным содержимым,
    скорее всего заменится на функцию, которая ничего не возвращает, ибо на кой'''
    file = open(file_name, 'r')
    decoded = file.read().encode('cp1251').decode('cp866')
    decoded_file = open('Workfile.txt', 'w')
    decoded_file.write(decoded)
    decoded_file.close()
    return decoded

def Find_Condition(decoded_file):
    '''Принимает на вход имя разкодированного файла,
    возвращает строку условия, каждый триплет отделен от арифметических знаков и скобок'''
    File = open(decoded_file, 'r')
    FoundCondition = ''
    Search = 'Поисковый образ'
    for i in range (1, 15):
        NameTriplet = str(File.readlines(i))
        if Search in NameTriplet:
            NameTriplet = str(File.readlines(i+1))[2:-2]
            FoundLine = NameTriplet
            break
    File.close()
    for i in range (len(FoundLine)):
        if FoundLine[i] == '/':
            break
        FoundCondition += FoundLine[i]
    for i in range(len(FoundCondition)):
        if FoundCondition[i] == '$' and FoundCondition[i-1] != ' ' and i != 0:
            FoundCondition = FoundCondition[0:i] + ' ' + FoundCondition[i:]
        elif FoundCondition[i].isalpha() == True and FoundCondition[i+1].isalpha() == False and FoundCondition[i+1] not in [' ', '.'] and i != len(FoundCondition):
            FoundCondition = FoundCondition[0:i+1] + ' ' + FoundCondition[i+1:]
    return FoundCondition

def Condition_add_triplet (condition):
    '''Добавляет в строку условия значения из треплетной строки, внутри запрос на ввод
    самой триплетной строки, если все еще имеются триплеты с '$' в условии, функция
    запрашивает ввод значения этих триплетов, есть защита ввода, вводит можно только числа.
    Функция возвращает обновленную строку условия'''
    conditionlist = condition.split(' ')
    triplet_line = input('Введите триплетную строку: ')
    triplet_list = triplet_line.split(';')
    for i in range(len(conditionlist)):
        if conditionlist[i] == '':
            conditionlist.pop([i])
    for i in range(len(conditionlist)):
        cond_check = 0
        for h in range (len(conditionlist[i])):
            if conditionlist[i][h] == '$':
                cond_check += 1
        if cond_check > 0:
            for j in range(len(triplet_list)):
                triplet_name = triplet_list[j].split('=')
                if conditionlist[i] == triplet_name[0]:
                    triplet_name = triplet_list[j].split('=')
                    conditionlist[i] = triplet_name[1]
    for i in range(len(conditionlist)):
        if conditionlist[i][0] == '$':
            while True:
                try:
                    need_input = input('Введите значение триплета ' + conditionlist[i] + ': ')
                    input_try = float(need_input)
                    break
                except ValueError:
                    print('Для ввода доступны только числа целые или дробные в формате X.X!')
            conditionlist[i] = need_input
    newcondition = ''
    for i in range (len(conditionlist)):
        newcondition += conditionlist[i] + ' '
    newcondition = newcondition[0:-1]
    return newcondition

#Проба
Dec = Decode_file('NARREZ.002')
Condition = Find_Condition('Workfile.txt')
print(Condition)
Conditionlist = Condition_add_triplet(Condition)
print(Conditionlist)
