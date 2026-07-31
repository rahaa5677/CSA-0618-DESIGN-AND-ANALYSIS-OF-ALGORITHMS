def bubble_sort_plain(arr):
    res = list(arr)
    n = len(res)
    comparisons = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res, comparisons

def bubble_sort_optimized(arr):
    res = list(arr)
    n = len(res)
    comparisons = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swapped = True
        if not swapped:
            break
    return res, comparisons

# Test Cases
alerts = [2,1,3,2,1,4,3,2,5,1,2,3,4,1,2] 
r1, c1 = bubble_sort_plain(alerts) 
r2, c2 = bubble_sort_optimized(alerts) 
assert r1 == r2 == sorted(alerts)     # both produce the same sorted result 
assert c2 <= c1                    	# optimized never does more comparisons 
print('Plain comparisons:', c1, '| Optimized comparisons:', c2) 
print('Bubble Sort Q4: All test cases passed!')
