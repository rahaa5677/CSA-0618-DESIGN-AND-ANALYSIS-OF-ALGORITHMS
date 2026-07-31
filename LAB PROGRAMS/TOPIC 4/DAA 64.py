def insert_song(playlist, new_song):
    res = list(playlist)
    res.append(new_song)
    n = len(res)
    
    key = res[n - 1] # format tracking: (title, length)
    j = n - 2
    while j >= 0 and res[j][1] > key[1]:
        res[j + 1] = res[j]
        j -= 1
    res[j + 1] = key
    
    return res

playlist = [('Intro', 120), ('Chill Beat', 210), ('Long Jam', 340)] #[cite: 1]
updated_playlist = insert_song(playlist, ('Quick Track', 180)) #[cite: 1]
durations = [s[1] for s in updated_playlist] #[cite: 1]
assert durations == sorted([120, 210, 340, 180]) #[cite: 1]
assert ('Quick Track', 180) in updated_playlist #[cite: 1]
print('Insertion Sort Q4: Passed!')
