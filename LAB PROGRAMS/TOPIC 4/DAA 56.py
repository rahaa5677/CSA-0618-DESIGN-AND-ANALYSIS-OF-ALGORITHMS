def optimized_bubble_sort(arr):
    res = list(arr)
    n = len(res)
    passes = 0
    
    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swapped = True
        # Early-exit optimization flag check[cite: 1]
        if not swapped:
            break
            
    return res, passes

sorted_rolls, passes = optimized_bubble_sort([101,102,104,103,105,107,106,108]) #[cite: 1]
assert sorted_rolls == sorted([101,102,104,103,105,107,106,108]) #[cite: 1]
assert passes < 8                            	# fewer than full n passes[cite: 1]
sorted_ok, passes_ok = optimized_bubble_sort([1,2,3,4,5])   # already sorted[cite: 1]
assert passes_ok == 1                        	# exits after first pass[cite: 1]
print('Bubble Sort Q1: Passed!')
