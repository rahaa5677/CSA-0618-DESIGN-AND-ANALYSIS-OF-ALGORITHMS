def string_match_first_occurrence(text, pattern):
    n, m = len(text), len(pattern)
    total_comparisons = 0
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            total_comparisons += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            print(f"First occurrence position: {i + 1}")
            print(f"Number of comparisons: {total_comparisons}")
            return i + 1, total_comparisons
            
    print("Pattern not found")
    return -1, total_comparisons

# Input validation based on document example[cite: 2]
string_match_first_occurrence("COMPUTERSCIENCE", "SCI")
