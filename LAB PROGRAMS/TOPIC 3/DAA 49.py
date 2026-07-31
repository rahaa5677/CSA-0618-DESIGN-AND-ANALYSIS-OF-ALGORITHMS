def string_match_visual_alignment(text, pattern):
    n, m = len(text), len(pattern)
    alignment_num = 0
    positions = []
    
    for i in range(n - m + 1):
        alignment_num += 1
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        
        res_str = "MATCH FOUND" if match else "MISMATCH"
        if match:
            positions.append(i + 1)
            
        print(f"\nAlignment {alignment_num}:")
        print(f"Text:    {text}")
        print(f"Pattern: {' ' * i}{pattern} -> {res_str}")
        
    print(f"\nPattern occurrence positions: {positions}")

# Input validation based on document example[cite: 2]
string_match_visual_alignment("ABCDABCABCDA", "ABCDA")
