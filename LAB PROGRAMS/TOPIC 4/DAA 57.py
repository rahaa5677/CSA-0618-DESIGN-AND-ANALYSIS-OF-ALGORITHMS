def bubble_sort_queue(queue):
    priority_map = {'ambulance': 3, 'bus': 2, 'car': 1} # Priority mappings[cite: 1]
    res = list(queue)
    n = len(res)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if priority_map[res[j]] < priority_map[res[j + 1]]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

queue = ['car', 'car', 'bus'] #[cite: 1]
queue.append('ambulance') #[cite: 1]
result = bubble_sort_queue(queue) #[cite: 1]
assert result == ['ambulance', 'bus', 'car', 'car']   #[cite: 1]
assert bubble_sort_queue(['ambulance']) == ['ambulance']   # single vehicle[cite: 1]
print('Bubble Sort Q2: Passed!')
