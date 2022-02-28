def InsertionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j] < arr[j-1]:
                swap(arr, j,j-1)
                j = j - 1
            else:
                break
    print(arr)

def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


InsertionSort([5, 4, 3, 2, 1])
