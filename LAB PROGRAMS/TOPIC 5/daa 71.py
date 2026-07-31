def find_min_max_temp(arr: list[int], low: int, high: int) -> tuple[int, int]:
    if low == high:
        return arr[low], arr[low]
        
    if high == low + 1:
        return (arr[high], arr[low]) if arr[low] > arr[high] else (arr[low], arr[high])
            
    mid = (low + high) // 2
    min1, max1 = find_min_max_temp(arr, low, mid)
    min2, max2 = find_min_max_temp(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

# Run verification
temps = [32, 28, 35, 25, 31, 29, 37]
min_t, max_t = find_min_max_temp(temps, 0, len(temps) - 1)
print(f"Minimum Temperature = {min_t} Maximum Temperature = {max_t}")
