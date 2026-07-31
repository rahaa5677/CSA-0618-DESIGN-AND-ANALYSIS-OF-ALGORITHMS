import math

def standard_multiply(A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def strassen_core(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2
    
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    
    M1 = strassen_core(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen_core(add_matrix(A21, A22), B11)
    M3 = strassen_core(A11, subtract_matrix(B12, B22))
    M4 = strassen_core(A22, subtract_matrix(B21, B11))
    M5 = strassen_core(add_matrix(A11, A12), B22)
    M6 = strassen_core(subtract_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen_core(subtract_matrix(A12, A22), add_matrix(B21, B22))
    
    C11 = add_matrix(subtract_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(add_matrix(subtract_matrix(M1, M2), M3), M6)
    
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    return C

def strassen_arbitrary_size(A, B):
    # Original dimensions
    rA, cA = len(A), len(A[0])
    rB, cB = len(B), len(B[0])
    
    # Determine maximum dimension bound
    max_dim = max(rA, cA, rB, cB)
    
    # Next highest power of 2
    pow2 = 1
    while pow2 < max_dim:
        pow2 *= 2
        
    # Pad input matrices with zeros
    A_padded = [[0] * pow2 for _ in range(pow2)]
    B_padded = [[0] * pow2 for _ in range(pow2)]
    
    for i in range(rA):
        for j in range(cA):
            A_padded[i][j] = A[i][j]
            
    for i in range(rB):
        for j in range(cB):
            B_padded[i][j] = B[i][j]
            
    # Compute using Strassen core
    C_padded = strassen_core(A_padded, B_padded)
    
    # Unpad/slice result back down to original size (rows of A by columns of B)
    C = [row[:cB] for row in C_padded[:rA]]
    return C

# Test Case 1: Identity/Matrix check for 5x5 matrix dimensions
A5 = [[i + j for j in range(5)] for i in range(5)]
B5 = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
assert strassen_arbitrary_size(A5, B5) == standard_multiply(A5, B5)

# Test Case 2: Non-Square Rectangular matrices (2x3 multiplied by 3x2)
A_rect = [[1, 2, 3], [4, 5, 6]]
B_rect = [[7, 8], [9, 10], [11, 12]]
assert strassen_arbitrary_size(A_rect, B_rect) == standard_multiply(A_rect, B_rect)

print("All test cases passed!")
