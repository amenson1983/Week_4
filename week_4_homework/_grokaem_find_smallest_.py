def find_Smallest(arr):

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

if __name__ == '__main__':
    arr = [56,67,89]
    index_smallest = find_Smallest(arr)
    print(index_smallest)