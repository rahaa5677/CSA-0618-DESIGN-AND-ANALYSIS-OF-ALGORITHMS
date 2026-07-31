def pick_up_card(hand, new_card):
    res = list(hand)
    res.append(new_card)
    n = len(res)
    
    key = res[n - 1]
    j = n - 2
    while j >= 0 and res[j] > key:
        res[j + 1] = res[j]
        j -= 1
    res[j + 1] = key
    
    return res

hand = []
for card in [7, 2, 9, 4, 1]: #[cite: 1]
    hand = pick_up_card(hand, card) #[cite: 1]
assert hand == sorted([7, 2, 9, 4, 1])   #[cite: 1]
assert pick_up_card([], 5) == [5]     # first card setup[cite: 1]
print('Insertion Sort Q2: Passed!')
