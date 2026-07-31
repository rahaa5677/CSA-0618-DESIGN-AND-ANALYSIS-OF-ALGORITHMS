def bubble_sort_with_frames(arr):
    res = list(arr)
    n = len(res)
    frames = [list(res)] # Capture starting structural snapshot[cite: 1]
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
        frames.append(list(res)) # Snapshot after completion of loop pass[cite: 1]
        
    return frames

frames = bubble_sort_with_frames([5, 1, 4, 2, 8]) #[cite: 1]
assert frames[-1] == sorted([5, 1, 4, 2, 8])   # final frame is sorted[cite: 1]
assert frames[0] == [5, 1, 4, 2, 8]         	# first frame is original input[cite: 1]
assert len(frames) >= 2                      	# at least an initial and final frame[cite: 1]
print('Bubble Sort Q3: Passed!')
