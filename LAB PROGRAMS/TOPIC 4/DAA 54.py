def distribute_prizes(participants):
    arr = list(participants)
    n = len(arr)
    
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            # Sort by score (index 1 of tuple) in descending order[cite: 1]
            if arr[j][1] > arr[max_idx][1]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        
    return arr

ranking = distribute_prizes([('Asha',88), ('Ravi',95), ('Meera',79), ('Dev',95)]) #[cite: 1]
scores_only = [p[1] for p in ranking] #[cite: 1]
assert scores_only == sorted(scores_only, reverse=True)   # descending order[cite: 1]
assert ranking[0][1] == 95                             	# top score first[cite: 1]
print('Selection Sort Q4: Passed!')
