def matrix_multiplication_logic(matrix_A, matrix_B):
    # 1. Dimensions Setup
    # Matrix A has shape (rows_A x cols_A)
    rows_A = len(matrix_A)
    cols_A = len(matrix_A[0])
    
    # Matrix B has shape (rows_B x cols_B)
    rows_B = len(matrix_B)
    cols_B = len(matrix_B[0])
    
    # 2. The Golden Rule Check
    # The width of A MUST equal the height of B
    if cols_A != rows_B:
        return "Error: Columns of A must equal Rows of B!"
        
    # 3. Create the Blank Canvas
    # The result will always have the height of A and the width of B
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # 4. The Logic Engine (The 3 Loops)
    
    # Loop 1 (i): Select a row from Matrix A
    for i in range(rows_A):
        
        # Loop 2 (j): Select a column from Matrix B
        for j in range(cols_B):
            
            # Loop 3 (k): The "Walker"
            # Moves Left-to-Right across Row 'i' in Matrix A
            # AND simultaneously moves Top-to-Bottom down Column 'j' in Matrix B
            for k in range(cols_A):
                
                # Multiply matching pairs and add them to the running total
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
                
    return result

# --- Verification ---

# Matrix A (2x2)
A = [
    [1, 2],
    [3, 4]
]

# Matrix B (2x2)
B = [
    [5, 6],
    [7, 8]
]

final_output = matrix_multiplication_logic(A, B)
print("Result Matrix:")
for row in final_output:
    print(row)
