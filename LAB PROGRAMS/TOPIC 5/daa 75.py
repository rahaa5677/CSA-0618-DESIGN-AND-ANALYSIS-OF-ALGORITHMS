def find_min_max_height(arr: list[int], low: int, high: int) -> tuple[int, int]:
    if low == high:
        return arr[low], arr[low]
        
    if high == low + 1:
        return (arr[high], arr[low]) if arr[low] > arr[high] else (arr[low], arr[high])
            
    mid = (low + high) // 2
    min1, max1 = find_min_max_height(arr, low, mid)
    min2, max2 = find_min_max_height(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

# Run verification
heights = [120, 150, 98, 175, 140, 165, 110, 190, 130, 145]
min_h, max_h = find_min_max_height(heights, 0, len(heights) - 1)
print(f"Minimum Height = {min_h} Maximum Height = {max_h}")
