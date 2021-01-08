

def capitalize_first():
    frase = input("Put a frase:")
    frase = frase.split()
    frase_new = ''
    for ch in frase:
        ch = ch[0].capitalize() + ch[1:]
        frase_new += ch + ' '
    print(str(frase_new))

def most_often_lett():
    frase = input("Put a frase:")
    frase1 = frase.rstrip(' ')
    x = 0
    max_ = 0
    max_lett = []
    for ch in frase1:
        x = frase1.find(ch)
        max_lett.append(x)

    return max_lett,frase

def point_quant_max(unique_list,indexes_list):
   max = 0
   max_ind = 0
   unique_quantity = 0
   for index in range(0,len(unique_list)-1):
       unique_quantity = indexes_list.count(unique_list[index])
       if unique_quantity>=max:
            max = unique_quantity
            max_ind = unique_list[index]
   return max_ind

if __name__ == '__main__':
   indexes_list,frase = most_often_lett()
   unique_list = set(indexes_list)
   unique_list = list(unique_list)

   max_index = point_quant_max(unique_list, indexes_list)



   print(frase,unique_list,max_index,frase[max_index])

