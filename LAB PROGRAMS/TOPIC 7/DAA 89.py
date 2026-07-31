import math

def count_multiplications_standard(n):
    # Standard multiplication requires exactly n^3 multiplications
    return n ** 3

def count_multiplications_strassen(n):
    # Strassen's requires 7^k multiplications where 2^k is the padded matrix size
    if n == 1:
        return 1
    # Find next power of two size k
    k = math.ceil(math.log2(n))
    return 7 ** k

# Verification Test Cases
assert count_multiplications_strassen(2) == 7
assert count_multiplications_standard(2) == 8
assert count_multiplications_strassen(4) == 49
assert count_multiplications_standard(4) == 64
assert count_multiplications_strassen(64) < count_multiplications_standard(64)

print("All test cases passed!")
