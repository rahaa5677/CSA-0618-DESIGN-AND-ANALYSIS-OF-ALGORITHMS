def binary_search_q1(arr: list[int], key: int) -> None:
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            print(f"Element found at position {mid + 1}")
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    print("Element not found")

# Test Case 1
binary_search_q1([5, 10, 20, 30, 40, 50], 30)

# Test Case 2
binary_search_q1([5, 10, 20, 30, 40, 50], 25)
