def count_inversions(arr):
    """Wrapper function to initiate the modified merge sort process."""
    # We pass a copy of the array to preserve the original input structure
    _, inversion_count = merge_sort_and_count(arr.copy())
    return inversion_count

def merge_sort_and_count(arr):
    # Base case: 0 or 1 elements have no inversions
    if len(arr) <= 1:
        return arr, 0
        
    mid = len(arr) // 2
    
    # Divide phase: recursively count inversions in both halves
    left_sorted, left_count = merge_sort_and_count(arr[:mid])
    right_sorted, right_count = merge_sort_and_count(arr[mid:])
    
    # Conquer phase: merge sorted halves and count split inversions
    merged_arr, split_count = merge_and_count_split(left_sorted, right_sorted)
    
    # Total inversions = left + right + split
    total_inversions = left_count + right_count + split_count
    return merged_arr, total_inversions

def merge_and_count_split(left, right):
    sorted_arr = []
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array
    split_inversions = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            # If left[i] > right[j], then all remaining elements in left 
            # (from index i to the end) form an inversion pair with right[j]
            sorted_arr.append(right[j])
            split_inversions += (len(left) - i)
            j += 1
            
    # Clean up remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr, split_inversions

# --- Test Case ---
test_array = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(test_array))
# Output: 3
