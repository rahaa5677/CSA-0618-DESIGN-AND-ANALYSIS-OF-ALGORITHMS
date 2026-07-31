def insert_song(playlist, new_song):
    res = list(playlist)
    res.append(new_song)
    n = len(res)
    
    key = res[n - 1] # structure: (name, duration)
    j = n - 2
    while j >= 0 and res[j][1] > key[1]:
        res[j + 1] = res[j]
        j -= 1
    res[j + 1] = key
    
    return res

# Test Cases
playlist = [('Intro', 120), ('Chill Beat', 210), ('Long Jam', 340)] 
updated_playlist = insert_song(playlist, ('Quick Track', 180)) 
durations = [s[1] for s in updated_playlist] 
assert durations == sorted([120, 210, 340, 180]) 
assert ('Quick Track', 180) in updated_playlist 
print('Insertion Sort Q4: All test cases passed!')
