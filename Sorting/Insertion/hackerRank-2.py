def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]

        while arr[i-1] > key and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

        print(*arr)





data = [3, 4, 7, 5, 6, 2, 1]

insertionSort(data)
