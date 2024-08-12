def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


input_str = input("Enter numbers separated by spaces: ")
arr = list(map(int, input_str.split()))
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)

