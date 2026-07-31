def find_all_pattern_occurrences(text, pattern):
    n, m = len(text), len(pattern)
    positions = []
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i + 1)
            
    print(f"Occurrences at positions {', '.join(map(str, positions))}.")
    return positions

# Input validation based on document example[cite: 2]
find_all_pattern_occurrences("BANANABANANA", "ANA")
