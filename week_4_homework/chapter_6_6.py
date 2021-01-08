import random

from Lesson_w04.week_4_homework.chapter_6_2_first_5_rows import rows_from_file_names_sum_count


def new_whole_row():
    myfile = open('rand.txt','w')
    quantity = int(input('Put quantity of random values:'))
    count = 0
    while count <=quantity-1:
        value = random.randrange(0,501)
        myfile.write(str(value) + '\n')
        count +=1
    myfile.close()

if __name__ == '__main__':
    #new_whole_row()
    sum, count = rows_from_file_names_sum_count()
    print(sum, count)