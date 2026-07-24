def linear_search(arr, key):
    """
    Linearly scans the array to find the given key.
    Returns the index if found, otherwise returns -1.
    """
    for index in range(len(arr)):
        if arr[index] == key:
            return index  # Key found, return its position
            
    return -1  # Key not found after scanning the whole array

# Sample Input
sample_array = [10, 25, 30, 45, 50]
search_key = 30

# Execute search
result = linear_search(sample_array, search_key)

# Sample Output Formatting
if result != -1:
    print(f"Key found at index {result}")
else:
    print("Key not found in the array")
