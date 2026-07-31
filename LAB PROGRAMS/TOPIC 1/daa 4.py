def fibonacci_loop(n):
    """Generates a Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Initialize the series with the first two terms
    series = [0, 1]
    
    # Generate subsequent terms
    while len(series) < n:
        next_term = series[-1] + series[-2]
        series.append(next_term)
        
    return series

# Example usage: Generate the first 10 numbers
print(fibonacci_loop(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
