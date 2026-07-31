def insertion_sort(arr):
    # Start from the second element (index 1) up to the end
    for i in range(1, len(arr)):
        key = arr[i]       # The item we want to position
        j = i - 1          # Look at elements to the left of the key
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1               # Move left to check the next element
            
        # Insert the key into its correct empty slot
        arr[j + 1] = key
        
    return arr

# --- Test Case ---
unsorted_array = [12, 11, 13, 5, 6]
print("Sorted Array:", insertion_sort(unsorted_array))
# Output: [5, 6, 11, 12, 13]
