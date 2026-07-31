import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged

def measure_time(arr):
    start_time = time.perf_counter()
    sorted_arr = merge_sort(arr)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print(f"Output : {','.join(map(str, sorted_arr))} Time Taken : ~{elapsed:.5f} sec")

# Test Case 1: Reverse Sorted Array
measure_time([9, 8, 7, 6, 5, 4, 3])

# Test Case 2: Sorted Array
measure_time([1, 2, 3, 4, 5, 6])
