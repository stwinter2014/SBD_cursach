condition = '$L.IR <= L.IR & ( $Z.D <= O.DNST ! $D.D <= O.DNST )'
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
        
print(conditionlist)
