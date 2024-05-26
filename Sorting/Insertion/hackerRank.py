def insertionSort(arr):
    n = len(arr)
    i = n-1

    while i > 0:
        if arr[i] < arr[i-1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            print(*arr)

            arr[i-1] = temp
            i -= 1

        else:
            break
    print(*arr)


data = [1,2,4,5,3]

insertionSort(data)

