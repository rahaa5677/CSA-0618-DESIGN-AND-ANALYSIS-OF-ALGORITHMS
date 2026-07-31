def selection_sort_min_writes(readings):
    arr = list(readings)
    n = len(arr)
    swap_count = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Only perform a swap and count a write if the element isn't already in place
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap_count += 1
            
    return arr, swap_count

# Test Cases
res, sw = selection_sort_min_writes([23.5, 19.2, 25.1, 18.8, 21.4]) 
assert res == sorted([23.5, 19.2, 25.1, 18.8, 21.4]) 
assert sw <= len(res) - 1           	# write bound holds   

res2, sw2 = selection_sort_min_writes([1, 2, 3, 4, 5]) 
assert sw2 == 0                          # already sorted -> zero swaps 
print('Selection Sort Q2: All test cases passed!')
