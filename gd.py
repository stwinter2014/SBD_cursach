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
for i in range(len(FoundCondition)):
    if FoundCondition[i] == '$' and FoundCondition[i-1] != ' ' and i != 0:
        FoundCondition = FoundCondition[0:i] + ' ' + FoundCondition[i:]
    elif FoundCondition[i].isalpha() == True and FoundCondition[i+1].isalpha() == False and FoundCondition[i+1] not in [' ', '.'] and i != len(FoundCondition):
        print('da')
        FoundCondition = FoundCondition[0:i+1] + ' ' + FoundCondition[i+1:]
print(FoundCondition)
