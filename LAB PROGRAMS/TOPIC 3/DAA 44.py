def string_match_character_metrics(text, pattern):
    n, m = len(text), len(pattern)
    total_comparisons = 0
    total_matches = 0
    total_mismatches = 0
    
    for i in range(n - m + 1):
        for j in range(m):
            total_comparisons += 1
            if text[i + j] == pattern[j]:
                total_matches += 1
            else:
                total_mismatches += 1
                break
                
    print(f"Total character comparisons = {total_comparisons}")
    print(f"Total matches = {total_matches}")
    print(f"Total mismatches = {total_mismatches}")
    return total_comparisons, total_matches, total_mismatches

# Input validation based on document example[cite: 2]
string_match_character_metrics("ABABABABAB", "ABAB")
