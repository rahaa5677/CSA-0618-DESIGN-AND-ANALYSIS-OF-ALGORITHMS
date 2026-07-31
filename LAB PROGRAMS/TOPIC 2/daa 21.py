def bubble_sort_queue(queue):
    # Mapping priorities: higher number = higher urgency
    priority_map = {'ambulance': 3, 'bus': 2, 'car': 1}
    
    res = list(queue)
    n = len(res)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Sort descending by priority mappings
            if priority_map[res[j]] < priority_map[res[j + 1]]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

# Test Cases
queue = ['car', 'car', 'bus'] 
queue.append('ambulance') 
result = bubble_sort_queue(queue) 
assert result == ['ambulance', 'bus', 'car', 'car']   
assert bubble_sort_queue(['ambulance']) == ['ambulance']   # single vehicle 
print('Bubble Sort Q2: All test cases passed!')
