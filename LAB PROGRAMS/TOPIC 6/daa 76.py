def merge_sort_count(arr):
    comparison_count = 0

    def sort_and_merge(sub_arr):
        nonlocal comparison_count
        if len(sub_arr) <= 1:
            return sub_arr
        
        mid = len(sub_arr) // 2
        left = sort_and_merge(sub_arr[:mid])
        right = sort_and_merge(sub_arr[mid:])
        
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparison_count += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_arr = sort_and_merge(arr)
    return sorted_arr, comparison_count

# Test Case 1
a1 = [12, 4, 78, 23, 45, 67, 89, 1]
res1, comp1 = merge_sort_count(a1)
print(f"Output : {','.join(map(str, res1))} Comparisons : {comp1}")

# Test Case 2
a2 = [5, 2, 9, 1, 6, 3]
res2, comp2 = merge_sort_count(a2)
print(f"Output : {','.join(map(str, res2))} Comparisons : {comp2}")
