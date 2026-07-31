def find_min_max_time(arr: list[int], low: int, high: int) -> tuple[int, int]:
    if low == high:
        return arr[low], arr[low]
        
    if high == low + 1:
        return (arr[high], arr[low]) if arr[low] > arr[high] else (arr[low], arr[high])
            
    mid = (low + high) // 2
    min1, max1 = find_min_max_time(arr, low, mid)
    min2, max2 = find_min_max_time(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

# Run verification
times = [14, 12, 18, 11, 15, 13, 17, 16, 10]
fastest, slowest = find_min_max_time(times, 0, len(times) - 1)
print(f"Fastest Time = {fastest} Slowest Time = {slowest}")
