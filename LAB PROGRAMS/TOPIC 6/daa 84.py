def external_merge(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

# Test Case 1
print(f"Output : {','.join(map(str, external_merge([1, 3, 5], [2, 4, 6])))}")

# Test Case 2
print(f"Output : {','.join(map(str, external_merge([10, 20], [5, 15, 25])))}")
