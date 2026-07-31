def bubble_sort_with_frames(arr):
    res = list(arr)
    n = len(res)
    frames = [list(res)] # Initial frame configuration
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
        frames.append(list(res))
        
    return frames

# Test Cases
frames = bubble_sort_with_frames([5, 1, 4, 2, 8]) 
assert frames[-1] == sorted([5, 1, 4, 2, 8])   # final frame is sorted 
assert frames[0] == [5, 1, 4, 2, 8]         	# first frame is the original input 
assert len(frames) >= 2                      	# at least an initial and final frame 
print('Bubble Sort Q3: All test cases passed!')
