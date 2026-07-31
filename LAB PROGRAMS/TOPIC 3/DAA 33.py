def find_first_occurrence(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"First occurrence at position {i + 1}")
            return i + 1
    print("Element not found")
    return -1

# Input validation based on document example[cite: 2]
arr = [10, 25, 15, 25, 30, 25, 40]
find_first_occurrence(arr, 25)
