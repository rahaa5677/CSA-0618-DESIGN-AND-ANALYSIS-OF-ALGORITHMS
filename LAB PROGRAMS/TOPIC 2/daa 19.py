def distribute_prizes(participants):
    # Operating on a copy of the list
    arr = list(participants)
    n = len(arr)
    
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            # Sort by score (index 1 of tuple) descending
            if arr[j][1] > arr[max_idx][1]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        
    return arr

# Test Cases
ranking = distribute_prizes([('Asha',88), ('Ravi',95), ('Meera',79), ('Dev',95)]) 
scores_only = [p[1] for p in ranking] 
assert scores_only == sorted(scores_only, reverse=True)   # descending order 
assert ranking[0][1] == 95                             	# top score first 
print('Selection Sort Q4: All test cases passed!')
