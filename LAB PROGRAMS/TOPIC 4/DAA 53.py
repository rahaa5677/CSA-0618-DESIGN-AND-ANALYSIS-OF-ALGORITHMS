def reorder_shelf(books):
    arr = list(books)
    n = len(arr)
    moves = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            moves += 1
            
    return arr, moves

ordered, moves = reorder_shelf([305, 102, 250, 118, 199, 400, 101]) #[cite: 1]
assert ordered == sorted([305, 102, 250, 118, 199, 400, 101]) #[cite: 1]
assert moves <= len(ordered) - 1   #[cite: 1]
ordered2, moves2 = reorder_shelf([100, 200, 300])   # already sorted[cite: 1]
assert moves2 == 0 #[cite: 1]
print('Selection Sort Q3: Passed!')
