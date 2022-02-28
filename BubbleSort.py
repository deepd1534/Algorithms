def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
    print(arr)


def swap(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


BubbleSort([7,2,4,9,1,-7,4,0,-4,-34])