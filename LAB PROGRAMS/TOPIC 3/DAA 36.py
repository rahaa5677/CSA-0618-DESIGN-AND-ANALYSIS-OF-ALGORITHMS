def sentinel_search(arr, key):
    n = len(arr)
    if n == 0:
        return -1, 0
        
    # Standard linear search tracking comparison count
    ordinary_comps = 0
    for i in range(n):
        ordinary_comps += 1
        if arr[i] == key:
            break

    # Sentinel implementation to avoid checking index bounds inside loop
    arr_copy = list(arr)
    last_element = arr_copy[-1]
    arr_copy[-1] = key
    
    sentinel_comps = 0
    i = 0
    while True:
        sentinel_comps += 1
        if arr_copy[i] == key:
            break
        i += 1
        
    # Restore and evaluate real placement
    arr_copy[-1] = last_element
    
    if i < n - 1 or arr[-1] == key:
        print(f"Position found: {i + 1}")
        print(f"Comparison count (Sentinel loop checks): {sentinel_comps}")
        return i + 1, sentinel_comps
    else:
        print("Position not found")
        return -1, sentinel_comps

# Input validation based on document example[cite: 2]
arr = [14, 9, 22, 35, 18, 41, 27]
sentinel_search(arr, 18)
