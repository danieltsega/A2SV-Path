def selectionSort(arr):
    for i in range(len(arr)-1):
        min_val = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_val]:
                min_val = j

        if min_val != i:
            arr[min_val], arr[i] = arr[i], arr[min_val]


    return arr



data = [4, 6, 2, 8, 7]

print("Original Data: ", data)

selectionSort(data)

print("Sorted Data:   ", data)
