def merge_sort(arr):
    # Base case: A list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # 1. DIVIDE: Find the midpoint and split the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # 2. CONQUER & MERGE: Combine the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_arr = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list

    # Compare elements from both lists and pick the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # If there are remaining elements in left or right, gather them
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# --- Test Case ---
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(unsorted_list))
# Output: [3, 9, 10, 27, 38, 43, 82]
