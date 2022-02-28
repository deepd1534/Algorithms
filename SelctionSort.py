def SelectionSort(arr):
    for i in range(len(arr)):
        last_index = len(arr)-i-1
        max_index = max_index_find(arr,last_index)
        swap(arr,last_index,max_index)
    print(arr)

def max_index_find(arr,last_index):
    start = 0
    for i in range(last_index+1):
        if arr[start] < arr[i]:
            start = i
    return start


def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp

SelectionSort([7,6,5,4,3,2,1,45,78,-90,0,12,45,78,23])