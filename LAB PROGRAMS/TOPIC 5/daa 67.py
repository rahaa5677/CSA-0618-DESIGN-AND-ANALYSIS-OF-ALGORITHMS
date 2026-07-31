def binary_search_q2(arr: list[int], key: int) -> int:
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            print(f"Index = {mid}")
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    print("Index = -1")
    return -1

# Test Case 1
binary_search_q2([2, 4, 6, 8, 10, 12], 8)

# Test Case 2
binary_search_q2([2, 4, 6, 8, 10, 12], 5)
