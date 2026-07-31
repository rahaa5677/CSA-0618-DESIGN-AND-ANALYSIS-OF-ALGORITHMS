def string_match_case_insensitive(text, pattern):
    # Normalize string data uniformly before processing
    text_lower = text.lower()
    pattern_lower = pattern.lower()
    
    n, m = len(text_lower), len(pattern_lower)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text_lower[i + j] != pattern_lower[j]:
                match = False
                break
        if match:
            print(f"Pattern found position: {i + 1}")
            return i + 1
            
    print("Pattern not found")
    return -1

# Input validation based on document example[cite: 2]
string_match_case_insensitive("DataStructuresAndAlgorithms", "ALGORITHMS")
