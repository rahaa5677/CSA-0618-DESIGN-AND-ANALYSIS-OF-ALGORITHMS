def sequential_search_basic(arr, key):
    # Search loop matching human/1-based positioning from specification
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            print(f"Element found at position {i + 1}")
            print(f"Number of comparisons = {comparisons}")
            return i + 1, comparisons
    return -1, comparisons

# Input validation based on document example[cite: 2]
arr = [12, 25, 8, 45, 32, 19, 50]
sequential_search_basic(arr, 32)
