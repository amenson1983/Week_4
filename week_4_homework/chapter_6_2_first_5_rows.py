#Вывод на экран верхней части файла. Напишите программу, которая
# запрашивает #у пользователя имя файла.
# Программа должна вывести на экран только первые пять строк #содержимого файла.
# Если в файле меньше пяти строк, то она должна вывести на экран #все содержимое файла.
def newone():
    my_file = open('testing.txt','w')
    my_file.write('John' + '\n')
    my_file.write('Jack' + '\n')
    my_file.write('Daniel' + '\n')
    my_file.write('Pit' + '\n')
    my_file.write('Paul' + '\n')
    my_file.write('Sam' + '\n')
    my_file.close()

def five_rows_from_file():

    filename = input('Put filename')
    my_file = open(filename,'r')
    description = my_file.readline()
    count = 0
    while description != ''and count <5:
        description = description.rstrip('\n')
        count +=1
        print(description)
        description = my_file.readline()
    my_file.close()

def rows_from_file_numerated():
    filename = input('Put filename')
    my_file = open(filename,'r')
    description = my_file.readline()
    count = 0
    while description != '':
        description = description.rstrip('\n')
        count +=1
        print(count,': ',description)
        description = my_file.readline()
    my_file.close()

def rows_from_file_names_count():
    filename = input('Put filename')
    my_file = open(filename,'r')
    description = my_file.readline()
    count = 0
    while description != '':
        description = description.rstrip('\n')
        count +=1

        description = my_file.readline()
    my_file.close()
    return count

def rows_from_file_names_sum_count():
    filename = input('Put filename')
    my_file = open(filename,'r')
    description = my_file.readline()
    count = 0
    sum = 0
    while description != '':
        description = description.rstrip('\n')
        count +=1
        sum += int(description)
        description = my_file.readline()
    my_file.close()
    return  sum, count

def new_whole_row():
    myfile = open('whole.txt','w')
    myfile.write('15' + '\n')
    myfile.write('13' + '\n')
    myfile.write('12' + '\n')
    myfile.write('18' + '\n')
    myfile.write('19' + '\n')
    myfile.write('24' + '\n')
    myfile.write('28' + '\n')
    myfile.write('33' + '\n')
    myfile.write('15' + '\n')
    myfile.write('16' + '\n')
    myfile.close()

if __name__ == '__main__':

    #five_rows_from_file()
    #rows_from_file_numerated()
    #x = rows_from_file_names_count()
    #print(x)
    #new_whole_row()
    sum, count = rows_from_file_names_sum_count()
    try:
        average = sum / count
        print(sum, count, average)
    except: ZeroDivisionError: print('Oh no, we can`t divide by zero')

