def insert_price(prices, new_price):
    res = list(prices)
    res.append(new_price)
    n = len(res)
    
    key = res[n - 1]
    j = n - 2
    while j >= 0 and res[j] > key:
        res[j + 1] = res[j]
        j -= 1
    res[j + 1] = key
    
    return res

prices = []
for p in [102.5, 98.3, 105.1, 100.0, 97.8]: #[cite: 1]
    prices = insert_price(prices, p) #[cite: 1]
assert prices == sorted([102.5, 98.3, 105.1, 100.0, 97.8]) #[cite: 1]
assert prices[0] == min(prices) and prices[-1] == max(prices)   # O(1) min/max checks[cite: 1]
print('Insertion Sort Q3: Passed!')
