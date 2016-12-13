def Decode_file(file_name):
    file = open(file_name, 'r')
    decoded = file.read().encode('cp1251').decode('cp866')
    decoded_file = open('Workfile.txt', 'w')
    decoded_file.write(decoded)
    decoded_file.close()
    return decoded

def Find_Condition(decoded_file):
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
    return FoundCondition

def Condition_modif (condition):
    for i in range():
    conditionlist = condition.split(' ')
    triplet_line = input('Введите триплетную строку: ')
    triplet_list = triplet_line.split(';')
    for i in range(len(conditionlist)):
        if conditionlist[i] == '':
            conditionlist.pop([i])
    cond_check = 0
    for i in range(len(conditionlist)):
        for h in range (len(conditionlist[i])):
            if conditionlist[i][h] == '$':
                cond_check += 1
        if cond_check > 0:
            condition_name = conditionlist[i].split('=')
            for j in range(len(triplet_list)):
                triplet_name = triplet_list[j].split('=')
                if condition_name[0] == triplet_name[0]:
                    conditionlist[i] = triplet_list[j]
                
    return conditionlist


Dec = Decode_file('NARREZ.002')
Condition_Line = Find_Condition('Workfile.txt')

print(Condition_Line)
condition_list = Condition_modif(Condition_Line)
print(condition_list)

