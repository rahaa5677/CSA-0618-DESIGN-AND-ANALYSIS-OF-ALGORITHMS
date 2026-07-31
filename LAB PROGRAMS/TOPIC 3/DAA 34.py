def find_all_occurrences(arr, key):
    positions = []
    for i in range(len(arr)):
        if arr[i] == key:
            positions.append(i + 1)
            
    print("Occurrences at positions:")
    print(", ".join(map(str, positions)))
    print(f"Total occurrences = {len(positions)}")
    return positions

# Input validation based on document example[cite: 2]
arr = [7, 12, 7, 25, 18, 7, 30, 7]
find_all_occurrences(arr, 7)
