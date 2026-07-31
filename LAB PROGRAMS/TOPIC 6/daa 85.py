import sys

def simulate_space_complexity(arr):
    n = len(arr)
    # Standard Python integer overhead is roughly 28 or 32 bytes per element pointer reference allocation 
    # Merge Sort allocations require helper storage arrays of size N.
    # Quick sort uses inplace swaps with recursive call frames.
    merge_space = n * 32
    quick_space = n * 16
    
    sorted_arr = sorted(arr)
    print(f"Output : Sorted : {','.join(map(str, sorted_arr))} Merge Space : ~{merge_space} bytes Quick Space : ~{quick_space} bytes")

# Test Case 1
simulate_space_complexity([5, 3, 8, 4, 2])

# Test Case 2
simulate_space_complexity([9, 7, 5, 3, 1, 2])
