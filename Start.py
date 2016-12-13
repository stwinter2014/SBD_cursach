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

Dec = Decode_file('NARREZ.002')

Condition = Find_Condition('Workfile.txt')

print(Condition)
