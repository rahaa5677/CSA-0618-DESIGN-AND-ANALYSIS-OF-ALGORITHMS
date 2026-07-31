def analyze_string_match_case(text, pattern):
    n, m = len(text), len(pattern)
    total_comparisons = 0
    
    for i in range(n - m + 1):
        for j in range(m):
            total_comparisons += 1
            if text[i + j] != pattern[j]:
                break
                
    # Classify runtime case structure dynamically
    if total_comparisons == m:
        case_type = "Best Case"
    elif total_comparisons == (n - m + 1) * m:
        case_type = "Worst Case"
    else:
        case_type = "Average Case"
        
    print(f"Search Type classification: {case_type}")
    print(f"Number of comparisons performed: {total_comparisons}")
    return case_type, total_comparisons

# Input validation based on document example[cite: 2]
analyze_string_match_case("AAAAAAAAAB", "AAAAB")
