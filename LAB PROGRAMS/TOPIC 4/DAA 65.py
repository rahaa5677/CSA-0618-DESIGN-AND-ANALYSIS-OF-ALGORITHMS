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

log = [18.2, 18.5, 18.9, 17.9, 19.1, 19.4, 19.0] #[cite: 1]
sorted_log, shifts_nearly = insertion_sort_count_shifts(log) #[cite: 1]
assert sorted_log == sorted(log)   #[cite: 1]

import random
shuffled_log = log.copy()
random.shuffle(shuffled_log)
_, shifts_random = insertion_sort_count_shifts(shuffled_log) #[cite: 1]
print('Nearly-sorted shifts:', shifts_nearly, '| Random shifts:', shifts_random) #[cite: 1]
print('Insertion Sort Q5: Passed!')
