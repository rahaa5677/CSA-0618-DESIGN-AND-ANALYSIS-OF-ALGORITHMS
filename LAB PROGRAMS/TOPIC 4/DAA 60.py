def bubble_sort_hand(arr):
    res = list(arr)
    n = len(res)
    passes = 0
    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
                swapped = True
        if not swapped:
            break
    return res, passes

hand = [2, 4, 6, 8, 9, 11, 13] #[cite: 1]
hand.append(7)                      # incremental addition[cite: 1]
final_hand, passes_incremental = bubble_sort_hand(hand) #[cite: 1]
assert final_hand == sorted(hand)   #[cite: 1]

import random 
shuffled = hand.copy() 
random.shuffle(shuffled) 
_, passes_full = bubble_sort_hand(shuffled) #[cite: 1]
assert passes_incremental <= passes_full   # nearly-sorted structure exits early[cite: 1]
print('Bubble Sort Q5: Passed!')
