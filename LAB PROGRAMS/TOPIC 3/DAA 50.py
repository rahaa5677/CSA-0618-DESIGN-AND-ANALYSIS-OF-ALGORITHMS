def comprehensive_string_matcher(text, pattern):
    n, m = len(text), len(pattern)
    occurrences = []
    total_comparisons = 0
    
    print("--- Shifting/Matching Process ---")
    for i in range(n - m + 1):
        match = True
        segment_comps = 0
        
        for j in range(m):
            total_comparisons += 1
            segment_comps += 1
            if text[i + j] != pattern[j]:
                match = False
                break
                
        # Print ongoing shifts
        alignment_view = text[i:i+m]
        print(f"Shift {i:02d}: Checking text window '{alignment_view}' against pattern | Comps here: {segment_comps}")
        
        if match:
            occurrences.append(i + 1)

    print("\n" + "="*50)
    print("BRUTE FORCE STRING MATCHING RESULTS & ANALYSIS")
    print("="*50)
    print(f"All Occurrences (1-based indices): {occurrences}")
    print(f"Total Comparisons Made:            {total_comparisons}")
    print("-"*50)
    print("Best-case complexity:  O(m)     - Occurs when the first window matches instantly")
    print("                                  (or mismatches immediately on character 1 every shift).")
    print("Worst-case complexity: O(m * n) - Occurs when text and pattern contain highly redundant")
    print("                                  sequences forcing full window scans each time.")
    print("Space complexity:      O(1)     - Performed utilizing structural pointer offsets in-place.")

# Input validation based on document example[cite: 2]
text_sample = "TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT"
pattern_sample = "TATCTT"
comprehensive_string_matcher(text_sample, pattern_sample)
