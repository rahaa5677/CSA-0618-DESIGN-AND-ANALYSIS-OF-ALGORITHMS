def binary_search_q3(arr: list[int], key: int) -> None:
    low, high = 0, len(arr) - 1
    iterations = 0
    
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == key:
            print(f"Element found Iterations = {iterations}")
            return
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
            
    print(f"Element not found Iterations = {iterations}")

# Test Case 1
binary_search_q3([5, 10, 15, 20, 25, 30, 35], 25)

# Test Case 2
binary_search_q3([5, 10, 15, 20, 25, 30, 35], 40)
