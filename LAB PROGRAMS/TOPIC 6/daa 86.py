def quick_select(arr, k):
    def partition(sub_arr, low, high):
        pivot = sub_arr[high]
        i = low - 1
        for j in range(low, high):
            if sub_arr[j] <= pivot:
                i += 1
                sub_arr[i], sub_arr[j] = sub_arr[j], sub_arr[i]
        sub_arr[i + 1], sub_arr[high] = sub_arr[high], sub_arr[i + 1]
        return i + 1

    def select(sub_arr, low, high, k_idx):
        if low == high:
            return sub_arr[low]
            
        p_idx = partition(sub_arr, low, high)
        
        if p_idx == k_idx:
            return sub_arr[p_idx]
        elif p_idx > k_idx:
            return select(sub_arr, low, p_idx - 1, k_idx)
        else:
            return select(sub_arr, p_idx + 1, high, k_idx)

    # k is 1-indexed, convert to 0-indexed index value
    return select(arr.copy(), 0, len(arr) - 1, k - 1)

# Test Case 1
print(f"Output : {quick_select([7, 10, 4, 3, 20, 15], 3)}")

# Test Case 2
print(f"Output : {quick_select([12, 3, 5, 7, 19], 2)}")
