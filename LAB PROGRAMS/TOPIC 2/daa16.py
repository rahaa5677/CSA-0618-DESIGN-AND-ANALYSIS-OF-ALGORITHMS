def top_k_scores(scores, k):
    # Safety copy to avoid modifying the original array out-of-place requirement
    arr = list(scores)
    n = len(arr)
    
    # Adjust k if there are fewer items than requested
    iterations = min(k, n)
    
    # Repeatedly find the maximum and move it to the front
    for i in range(iterations):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        # Swap the maximum element to its final sorted position
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        
    return arr[:iterations]

# Test Cases
assert top_k_scores([72,88,65,90,77,95,60,83,91,68], 5) == [95,91,90,88,83] 
assert top_k_scores([5,3,1], 5) == [5,3,1]  	# fewer than k items 
assert top_k_scores([], 3) == []            	# empty input 
print('Selection Sort Q1: All test cases passed!')
