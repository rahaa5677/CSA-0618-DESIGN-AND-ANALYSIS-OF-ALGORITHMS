def sequential_search_profile(arr, keys):
    for key in keys:
        print(f"\n--- Searching for Key: {key} ---")
        comparisons = 0
        found = False
        for i in range(len(arr)):
            comparisons += 1
            print(f"  Comparison {comparisons}: Checking index {i} (Value: {arr[i]}) vs Key {key}")
            if arr[i] == key:
                print(f"  >> Match found at position {i + 1}!")
                found = True
                break
        if not found:
            print("  >> Element not found in full array scan.")
        print(f"Total comparisons performed = {comparisons}")

    # Complete Complexity Analysis Output[cite: 2]
    print("\n" + "="*40)
    print("SEQUENTIAL SEARCH COMPLEXITY ANALYSIS")
    print("="*40)
    print("Best-case complexity:    O(1)     - Element is at the first position.")
    print("Worst-case complexity:   O(n)     - Element is at the end or completely absent.")
    print("Average-case complexity: O(n)     - Element found mid-array on average ((n+1)/2 checks).")
    print("Space complexity:        O(1)     - Performed completely in-place.")

# Input validation based on document example[cite: 2]
arr = [45, 23, 67, 12, 89, 34, 56, 78, 90, 11, 29, 73, 18, 64, 37]
keys = [73, 18, 100]
sequential_search_profile(arr, keys)
