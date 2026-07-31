def compare_match_executions(text, p1, p2):
    def count_comps(p):
        n, m = len(text), len(p)
        comps = 0
        for i in range(n - m + 1):
            for j in range(m):
                comps += 1
                if text[i + j] != p[j]:
                    break
        return comps

    c1 = count_comps(p1)
    c2 = count_comps(p2)
    
    print(f"Successful Search (Pattern: '{p1}'): {c1} comparisons")
    print(f"Unsuccessful Search (Pattern: '{p2}'): {c2} comparisons")
    return c1, c2

# Input validation based on document example[cite: 2]
compare_match_executions("PROGRAMMINGLAB", "LAB", "TEST")
