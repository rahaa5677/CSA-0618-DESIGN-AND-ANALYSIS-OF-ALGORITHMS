def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def hybrid_merge_sort(arr, threshold=4):
    if len(arr) <= threshold:
        return insertion_sort(arr)
        
    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid], threshold)
    right = hybrid_merge_sort(arr[mid:], threshold)
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged

# Test Case 1
a1 = [12, 11, 13, 5, 6, 7, 3, 2]
print(f"Output : {','.join(map(str, hybrid_merge_sort(a1)))}")

# Test Case 2
a2 = [9, 4, 6, 2, 8, 1]
print(f"Output : {','.join(map(str, hybrid_merge_sort(a2)))}")
