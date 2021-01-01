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
    arr = [56,67,89,53,13,12,17,500]
    quick_sort_my(arr,0,len(arr)-1)
    print(arr)