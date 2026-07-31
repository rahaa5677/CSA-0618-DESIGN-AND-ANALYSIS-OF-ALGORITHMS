def find_min_max_marks(arr: list[int], low: int, high: int) -> tuple[int, int]:
    if low == high:
        return arr[low], arr[low]
        
    if high == low + 1:
        return (arr[high], arr[low]) if arr[low] > arr[high] else (arr[low], arr[high])
            
    mid = (low + high) // 2
    min1, max1 = find_min_max_marks(arr, low, mid)
    min2, max2 = find_min_max_marks(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

# Run verification
marks = [78, 92, 65, 88, 95, 72, 81, 69]
min_m, max_m = find_min_max_marks(marks, 0, len(marks) - 1)
print(f"Minimum Mark = {min_m} Maximum Mark = {max_m}")
