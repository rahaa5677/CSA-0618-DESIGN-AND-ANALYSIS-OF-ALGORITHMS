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

# Test Cases
hand = [2, 4, 6, 8, 9, 11, 13] 
hand.append(7)                      # nearly sorted: one new card 
final_hand, passes_incremental = bubble_sort_hand(hand) 
assert final_hand == sorted(hand)   

import random 
shuffled = hand.copy() 
random.seed(42) # Deterministic shuffle for tests
random.shuffle(shuffled) 
_, passes_full = bubble_sort_hand(shuffled) 
assert passes_incremental <= passes_full   # nearly-sorted needs no more passes 
print('Bubble Sort Q5: All test cases passed!')
