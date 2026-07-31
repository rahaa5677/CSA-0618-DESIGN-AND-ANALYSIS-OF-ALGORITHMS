def insert_updated_score(board, new_score):
    res = list(board)
    res.append(new_score)
    n = len(res)
    shifts = 0
    
    key = res[n - 1]
    j = n - 2
    # Sort descending for leaderboards[cite: 1]
    while j >= 0 and res[j] < key:
        res[j + 1] = res[j]
        shifts += 1
        j -= 1
    res[j + 1] = key
    
    return res, shifts

board = [980, 875, 760, 690, 500] #[cite: 1]
updated_board, shifts = insert_updated_score(board, 820) #[cite: 1]
assert updated_board == [980, 875, 820, 760, 690, 500]   #[cite: 1]
board2, shifts2 = insert_updated_score(board, 100) #[cite: 1]
assert board2[-1] == 100 and shifts2 == 0         	# lowest score goes to end without shifting[cite: 1]
print('Insertion Sort Q1: Passed!')
