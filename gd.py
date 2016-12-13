File = open('Workfile.txt', 'r')
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
FoundCondition_list = FoundCondition.split(' ')
print(FoundCondition)
ReadyCondition = []
for i in range (len(FoundCondition_list)):
    if FoundCondition_list[i] == '':
        FoundCondition_list.pop([i])
for i in range (len(FoundCondition_list)):
    check = 0
    for j in range (len(FoundCondition_list[i])):
        if FoundCondition_list[i][0] != '$' and FoundCondition_list[i][j] == '$':
            for h in range (len(FoundCondition_list[i])):
                if Found_Condition_list[i][h].isalpha() == False and Found_Condition_list[i][h] not in ['$', '.']:
            check += 1
    if check > 0:
        if
            Split = FoundCondition_list[i].split('$')
            ReadyCondition.append(Split[0])
            Split[1] = '$' + Split[1]
            ReadyCondition.append(Split[1])
    else:
        ReadyCondition.append(FoundCondition_list[i])
print(ReadyCondition)
