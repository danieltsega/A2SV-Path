# A python script dedicated to insertion sort algorithm

# create a function that does the logic of insertion
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]


        while arr[i-1] > key and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

data = [9, 5, 1, 4, 3]

insertion_sort(data)

print('Sorted Input: ')
print(data)
