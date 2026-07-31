def quick_sort_count(arr):
    comparison_count = 0

    def sort(sub_arr, low, high):
        nonlocal comparison_count
        if low < high:
            # Partitioning using last element as pivot
            pivot = sub_arr[high]
            i = low - 1
            for j in range(low, high):
                comparison_count += 1
                if sub_arr[j] <= pivot:
                    i += 1
                    sub_arr[i], sub_arr[j] = sub_arr[j], sub_arr[i]
            sub_arr[i + 1], sub_arr[high] = sub_arr[high], sub_arr[i + 1]
            p = i + 1
            
            sort(sub_arr, low, p - 1)
            sort(sub_arr, p + 1, high)

    arr_copy = arr.copy()
    sort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy, comparison_count

# Test Case 1
a1 = [38, 27, 43, 3, 9, 82, 10]
res1, comp1 = quick_sort_count(a1)
print(f"Output : {','.join(map(str, res1))} Comparisons : {comp1}")

# Test Case 2
a2 = [10, 7, 8, 9, 1]
res2, comp2 = quick_sort_count(a2)
print(f"Output : {','.join(map(str, res2))} Comparisons : {comp2}")
