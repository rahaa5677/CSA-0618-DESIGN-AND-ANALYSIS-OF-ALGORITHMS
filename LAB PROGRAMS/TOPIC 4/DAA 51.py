def top_k_scores(scores, k):
    # Safety copy to avoid modifying the original array out-of-place requirement[cite: 1]
    arr = list(scores)
    n = len(arr)
    iterations = min(k, n) # Adjust if there are fewer items than k[cite: 1]
    
    for i in range(iterations):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        
    return arr[:iterations]

assert top_k_scores([72,88,65,90,77,95,60,83,91,68], 5) == [95,91,90,88,83] #[cite: 1]
assert top_k_scores([5,3,1], 5) == [5,3,1]  	# fewer than k items[cite: 1]
assert top_k_scores([], 3) == []            	# empty input[cite: 1]
print('Selection Sort Q1: Passed!')
