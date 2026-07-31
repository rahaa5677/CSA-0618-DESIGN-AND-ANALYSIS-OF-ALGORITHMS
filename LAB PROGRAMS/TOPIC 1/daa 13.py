def max_subarray_sum(arr):
    # Edge case: if the array is empty, return 0
    if not arr:
        return 0
        
    # Initialize both tracking values with the first element
    current_max = arr[0]
    global_max = arr[0]
    
    # Iterate through the array starting from the second element
    for x in arr[1:]:
        # Decide whether to add x to the existing subarray or start fresh from x
        current_max = max(x, current_max + x)
        
        # Update our global record tracker if we found a new peak sum
        if current_max > global_max:
            global_max = current_max
            
    return global_max

# --- Test Case 1: Standard Array with Mixed Signs ---
test_arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Max Subarray Sum:", max_subarray_sum(test_arr1))
# Output: 6 
# (The optimal contiguous subarray is [4, -1, 2, 1], which sums to 6)

# --- Test Case 2: All Negative Numbers ---
test_arr2 = [-2, -3, -1, -5]
print("Max Subarray Sum (All Negative):", max_subarray_sum(test_arr2))
# Output: -1
# (The algorithm cleanly picks the single largest element [-1])
