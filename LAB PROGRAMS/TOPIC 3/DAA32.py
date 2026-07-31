def sequential_search_unsuccessful(arr, key):
    comparisons = 0
    found = False
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            found = True
            break
            
    if not found:
        print("Element not found")
        print(f"Number of comparisons = {comparisons}")
    return comparisons

# Input validation based on document example[cite: 2]
arr = [5, 10, 15, 20, 25, 30, 35]
sequential_search_unsuccessful(arr, 18)
