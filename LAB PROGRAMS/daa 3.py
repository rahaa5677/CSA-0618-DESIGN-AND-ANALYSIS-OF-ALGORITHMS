def factorial_iterative(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Execution
print(f"Iterative Output (n=8): {factorial_iterative(8)}")
