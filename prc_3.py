def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current position has the smallest element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Found a smaller element
        # Swap the found minimum with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

selection_sort(arr)

print("Sorted array:  ", arr)
