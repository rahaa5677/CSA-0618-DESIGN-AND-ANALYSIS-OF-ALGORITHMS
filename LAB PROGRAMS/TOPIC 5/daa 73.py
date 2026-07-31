def find_min_max_stock(arr: list[int], low: int, high: int) -> tuple[int, int]:
    if low == high:
        return arr[low], arr[low]
        
    if high == low + 1:
        return (arr[high], arr[low]) if arr[low] > arr[high] else (arr[low], arr[high])
            
    mid = (low + high) // 2
    min1, max1 = find_min_max_stock(arr, low, mid)
    min2, max2 = find_min_max_stock(arr, mid + 1, high)
    
    return min(min1, min2), max(max1, max2)

# Run verification
stocks = [450, 520, 480, 610, 430, 590]
min_s, max_s = find_min_max_stock(stocks, 0, len(stocks) - 1)
print(f"Minimum Stock Price = {min_s} Maximum Stock Price = {max_s}")
