def count_inversions(arr):
    inv_count = 0

    def merge_and_count(sub_arr):
        nonlocal inv_count
        if len(sub_arr) <= 1:
            return sub_arr
            
        mid = len(sub_arr) // 2
        left = merge_and_count(sub_arr[:mid])
        right = merge_and_count(sub_arr[mid:])
        
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                # All remaining elements in left slice are inversions
                inv_count += (len(left) - i)
                j += 1
                
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_arr = merge_and_count(arr)
    return sorted_arr, inv_count

# Test Case 1
res1, count1 = count_inversions([2, 4, 1, 3, 5])
print(f"Output : Sorted : {','.join(map(str, res1))} Inversions : {count1}")

# Test Case 2
res2, count2 = count_inversions([4, 3, 2, 1])
print(f"Output : Sorted : {','.join(map(str, res2))} Inversions : {count2}")
