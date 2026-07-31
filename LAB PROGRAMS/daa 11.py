def heapify(arr, n, i):
    """
    Turns a subtree rooted at index i into a Max-Heap.
    n is the size of the heap.
    """
    largest = i         # Initialize largest as root
    left = 2 * i + 1    # Left child index
    right = 2 * i + 2   # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # 1. Build a Max-Heap from the array data
    # We start from the last non-leaf node and work backwards to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to the end of the array
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call max heapify on the reduced heap to restore order at the root
        heapify(arr, i, 0)
        
    return arr

# --- Test Case ---
unsorted_array = [12, 11, 13, 5, 6, 7]
print("Sorted Array:", heap_sort(unsorted_array))
# Output: [5, 6, 7, 11, 12, 13]
