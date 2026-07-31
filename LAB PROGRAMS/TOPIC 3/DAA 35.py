def sequential_search_metrics(arr, key):
    total_comparisons = 0
    total_matches = 0
    total_mismatches = 0
    
    for x in arr:
        total_comparisons += 1
        if x == key:
            total_matches += 1
        else:
            total_mismatches += 1
            
    print(f"Total comparisons = {total_comparisons}")
    print(f"Total matches = {total_matches}")
    print(f"Total mismatches = {total_mismatches}")
    return total_comparisons, total_matches, total_mismatches

# Input validation based on document example[cite: 2]
arr = [3, 6, 9, 12, 15, 18, 21]
sequential_search_metrics(arr, 15)
