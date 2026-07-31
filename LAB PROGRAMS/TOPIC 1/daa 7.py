def quicksort_readable(arr):
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr
    
    # Selecting the middle element as the pivot
    pivot = arr[len(arr) // 2]
    
    # Partitioning arrays using list comprehensions
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the sub-arrays and combine them
    return quicksort_readable(left) + middle + quicksort_readable(right)

# Test Case
unsorted_list = [29, 10, 14, 37, 13, 2, 14]
print("Sorted Array:", quicksort_readable(unsorted_list))
# Output: [2, 10, 13, 14, 14, 29, 37]
