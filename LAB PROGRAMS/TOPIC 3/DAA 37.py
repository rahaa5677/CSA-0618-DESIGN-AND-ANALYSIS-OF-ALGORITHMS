def search_student_register(registers, key):
    for i in range(len(registers)):
        if registers[i] == key:
            print(f"Register Number found at position {i + 1}")
            return i + 1
    print("Register Number not found")
    return -1

# Input validation based on document example[cite: 2]
registers = [101, 102, 103, 104, 105, 106]
search_student_register(registers, 104)
