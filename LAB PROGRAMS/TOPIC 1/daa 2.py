def binary_search_recursive(arr, low, high, key):
    # Base case: the search space is exhausted (key not present)
    if low > high:
        return -1

    # Find the middle index
    mid = low + (high - low) // 2

    # Case 1: The middle element is the key
    if arr[mid] == key:
        return mid
    
    # Case 2: The key is smaller than mid, search the left half
    elif arr[mid] > key:
        return binary_search_recursive(arr, low, mid - 1, key)
    
    # Case 3: The key is larger than mid, search the right half
    else:
        return binary_search_recursive(arr, mid + 1, high, key)

# Sample Input
sample_array = [5, 10, 15, 20, 25]
search_key = 25

# Execute search (initially searching from index 0 to length - 1)
result = binary_search_recursive(sample_array, 0, len(sample_array) - 1, search_key)

# Sample Output Formatting
if result != -1:
    print(f"Key found at index {result}")
else:
    print("Key not found in the array")
