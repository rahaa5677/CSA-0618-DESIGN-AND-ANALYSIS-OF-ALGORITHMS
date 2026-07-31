def search_string_data(names, search_name):
    for i in range(len(names)):
        if names[i] == search_name:
            print(f"Name found at position {i + 1}")
            return i + 1
    print("Name not found")
    return -1

# Input validation based on document example[cite: 2]
names = ["Anu", "Bala", "Charan", "Deepa", "Esha", "Farhan"]
search_string_data(names, "Deepa")
