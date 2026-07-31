def brute_force_string_match(text, pattern):
    n, m = len(text), len(pattern)
    positions = []
    total_comparisons = 0
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            total_comparisons += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i + 1) # 1-based index placement[cite: 2]
            
    print(f"Position(s) where the pattern occurs: {positions}")
    print(f"Total number of comparisons: {total_comparisons}")
    return positions, total_comparisons

# Input validation based on document example[cite: 2]
brute_force_string_match("AABAACAADAABAABA", "AABA")
