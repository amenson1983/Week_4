def q_sort_grok(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i >= pivot]
        return q_sort_grok(less) + [pivot] + q_sort_grok(greater)

def marker_find(arr,start,end):
    marker = start
    for i in range(start,end+1):
        if arr[i] <= arr[end]:
            temp = arr[marker]
            arr[marker] = arr[i]
            arr[i] = temp
            marker +=1
    return marker-1

def q_sort_wmark(arr,start,end):
    if start >= end:
        return
    pivot = marker_find(arr,start,end)
    q_sort_wmark(arr, start, pivot-1)
    q_sort_wmark(arr, pivot+1, end)


if __name__ == '__main__' :
    arr = [11, 32, 23, 24, 15, 16, 6, 8, 9, 80,91]
    #arr = q_sort_grok(arr)
    q_sort_wmark(arr,0,int(len(arr))-1)
    print(arr)