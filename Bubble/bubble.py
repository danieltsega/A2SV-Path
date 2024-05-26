def bubbleSort(arr):

    n = len(arr)

    for i in range(n):

        
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]







data = [4,2,8,1,3,7]

print("Original Data: ", data)

bubbleSort(data)

print("=========================================")
print("=========================================")


print("Sorted Data:   ", data)
