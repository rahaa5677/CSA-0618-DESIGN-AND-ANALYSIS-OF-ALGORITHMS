def string_match_comparison_table(text, pattern):
    n, m = len(text), len(pattern)
    print(f"{'Shift':<10}{'Comparisons':<15}{'Result':<15}")
    print("-" * 40)
    
    for i in range(n - m + 1):
        comps_made = 0
        match = True
        for j in range(m):
            comps_made += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        res_str = "Match" if match else "Mismatch"
        print(f"{i:<10}{comps_made:<15}{res_str:<15}")

# Input validation based on document example[cite: 2]
string_match_comparison_table("MISSISSIPPI", "ISSI")
