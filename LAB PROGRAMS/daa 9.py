def gcd_euclidean_iterative(a, b):
    """Calculates the GCD of two numbers using a loop."""
    while b != 0:
        # a becomes b, and b becomes the remainder of a divided by b
        a, b = b, a % b
    return a

# Test Case
print("GCD of 48 and 18 is:", gcd_euclidean_iterative(48, 18))
# Output: 6
