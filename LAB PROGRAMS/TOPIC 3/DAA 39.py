def search_2d_matrix(matrix, key):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == key:
                print(f"Element found at Row {r + 1} Column {c + 1}")
                return r + 1, c + 1
    print("Element not found")
    return -1

# Input validation based on document example[cite: 2]
matrix = [
    [12, 8, 15],
    [5, 18, 27],
    [9, 11, 24]
]
search_2d_matrix(matrix, 24)
