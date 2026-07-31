def insert_updated_score(board, new_score):
    res = list(board)
    res.append(new_score)
    n = len(res)
    shifts = 0
    
    # Run the insertion step starting from the newly added last element
    key = res[n - 1]
    j = n - 2
    
    # Leaderboard tracks high scores first, sorting descending
    while j >= 0 and res[j] < key:
        res[j + 1] = res[j]
        shifts += 1
        j -= 1
    res[j + 1] = key
    
    return res, shifts

# Test Cases
board = [980, 875, 760, 690, 500] 
updated_board, shifts = insert_updated_score(board, 820) 
assert updated_board == [980, 875, 820, 760, 690, 500]   

board2, shifts2 = insert_updated_score(board, 100)   # lowest score 
assert board2[-1] == 100 and shifts2 == 0         	# no shifts needed, goes to the end 
print('Insertion Sort Q1: All test cases passed!')
