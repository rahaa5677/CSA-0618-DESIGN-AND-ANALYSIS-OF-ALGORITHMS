def insertion_sort_count_shifts(arr):
    res = list(arr)
    n = len(res)
    shifts = 0
    for i in range(1, n):
        key = res[i]
        j = i - 1
        while j >= 0 and res[j] > key:
            res[j + 1] = res[j]
            shifts += 1
            j -= 1
        res[j + 1] = key
    return res, shifts

# Test Cases
log = [18.2, 18.5, 18.9, 17.9, 19.1, 19.4, 19.0] 
sorted_log, shifts_nearly = insertion_sort_count_shifts(log) 
assert sorted_log == sorted(log)   

import random 
shuffled_log = log.copy() 
random.seed(42)
random.shuffle(shuffled_log) 
_, shifts_random = insertion_sort_count_shifts(shuffled_log) 
print('Nearly-sorted shifts:', shifts_nearly, '| Random shifts:', shifts_random) 
print('Insertion Sort Q5: All test cases passed!')
