from Lesson_w04.week_4_homework._grokaem_find_smallest_ import find_Smallest


def sorting(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        sorted_arr.append(arr.pop(smallest)) #интересный метод sorted_arr.append(arr.pop(smallest)) - находит, выдает и удаляет. Дальше без него
    return sorted_arr

def average():
    count = 13
    sum = 0
    for i in range(13):
        x = int(input("Put the mark:"))
        sum +=x
    average = sum / count
    return average

def sorting_recursion(arr,start,end):
    marker = start
    for i in range(start,end+1):
        if arr[i] <= arr[end]:
            temp = arr[marker]
            arr[marker] = arr[i]
            arr[i] = temp
            marker +=1

    return marker-1

def quick_sort_my(arr,start,end):
    if start >= end:
        return
    pivot = sorting_recursion(arr,start,end)
    quick_sort_my(arr, start, pivot-1)
    quick_sort_my(arr, pivot+1, end)



if __name__ == '__main__':
    arr = [56,67,89,53,13,12,17]
    quick_sort_my(arr,0,len(arr)-1)
    print(arr)