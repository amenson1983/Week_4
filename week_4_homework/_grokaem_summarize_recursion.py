def sum_recurs(arr):
    return sum_of_list_recursion(arr)

def sum_of_list_recursion(arr):
    if sum(arr) == 0:
        return 0
    else:
        return arr[0] + sum_recurs(arr[1:int(len(arr))])


if __name__ == '__main__' :
    arr = [1, 2, 3, 4, 5,6]
    #arr1 = arr[0] + sum(arr[0+1:int(len(arr))])
    x = sum_recurs(arr)

    #print()
    print(x)
    #print(arr)