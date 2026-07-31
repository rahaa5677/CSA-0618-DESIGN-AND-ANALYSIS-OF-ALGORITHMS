def selection_sort(arr):
    res = list(arr)
    n = len(res)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if res[j] < res[min_idx]:
                min_idx = j
        res[i], res[min_idx] = res[min_idx], res[i]
    return res

assert selection_sort([499,129,899,45,275,60,310,150]) == sorted([499,129,899,45,275,60,310,150]) #[cite: 1]
assert selection_sort([]) == []             	# empty list[cite: 1]
assert selection_sort([7]) == [7]            	# single item[cite: 1]
print('Selection Sort Q5: Passed!')
