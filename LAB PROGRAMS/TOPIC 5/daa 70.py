def binary_search_last_occurrence(arr: list[int], key: int) -> None:
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid
            low = mid + 1  # Keep looking right for later duplicates
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    if result != -1:
        print(f"Last occurrence at index {result}")
    else:
        print("Element not found")

# Test Case 1
binary_search_last_occurrence([1, 2, 2, 2, 3, 4, 5, 6], 2)

# Test Case 2
binary_search_last_occurrence([1, 2, 2, 2, 3, 4, 5, 6], 9)
