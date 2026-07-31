# Reusing algorithms from Q1 and Q2
def run_comparison(arr):
    # Merge Sort Execution
    m_comp = 0
    def m_sort(sub_arr):
        nonlocal m_comp
        if len(sub_arr) <= 1: return sub_arr
        mid = len(sub_arr) // 2
        left, right = m_sort(sub_arr[:mid]), m_sort(sub_arr[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            m_comp += 1
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged

    sorted_arr = m_sort(arr)

    # Quick Sort Execution
    q_comp = 0
    def q_sort(sub_arr, low, high):
        nonlocal q_comp
        if low < high:
            pivot = sub_arr[high]
            i = low - 1
            for j in range(low, high):
                q_comp += 1
                if sub_arr[j] <= pivot:
                    i += 1
                    sub_arr[i], sub_arr[j] = sub_arr[j], sub_arr[i]
            sub_arr[i + 1], sub_arr[high] = sub_arr[high], sub_arr[i + 1]
            p = i + 1
            q_sort(sub_arr, low, p - 1)
            q_sort(sub_arr, p + 1, high)

    q_arr = arr.copy()
    q_sort(q_arr, 0, len(q_arr) - 1)
    
    print(f"Output : Sorted Array : {','.join(map(str, sorted_arr))} Merge Comparisons : {m_comp} Quick Comparisons : {q_comp}")

# Test Case 1
run_comparison([12, 11, 13, 5, 6, 7])
# Test Case 2
run_comparison([4, 2, 6, 1, 3])
