import math

def distance(p1, p2):
    """Calculates Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    """Base case solver for 3 or fewer points."""
    min_dist = float('inf')
    pair = (None, None)
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair

def closest_strip(strip, delta, best_pair):
    """Finds the closest pair inside the middle strip."""
    min_dist = delta
    
    # Sort strip points by their Y-coordinate
    strip.sort(key=lambda point: point[1])
    
    # Check each point against neighboring points above it in Y-order
    for i in range(len(strip)):
        j = i + 1
        # Stop comparing if the vertical distance exceeds our current minimum delta
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                best_pair = (strip[i], strip[j])
            j += 1
            
    return min_dist, best_pair

def closest_pair_recursive(points_x):
    n = len(points_x)
    
    # Base case: if there are 3 or fewer points, use brute force
    if n <= 3:
        return brute_force(points_x)
        
    # Divide: split the array into left and right halves
    mid = n // 2
    mid_point = points_x[mid]
    
    left_half = points_x[:mid]
    right_half = points_x[mid:]
    
    # Conquer: find minimum distances in left and right halves
    dl, pair_l = closest_pair_recursive(left_half)
    dr, pair_r = closest_pair_recursive(right_half)
    
    # Determine the smaller of the two minimums
    if dl < dr:
        delta = dl
        best_pair = pair_l
    else:
        delta = dr
        best_pair = pair_r
        
    # Build the strip containing points within delta distance of the mid vertical line
    strip = [p for p in points_x if abs(p[0] - mid_point[0]) < delta]
    
    # Conquer the strip
    ds, pair_s = closest_strip(strip, delta, best_pair)
    
    return ds, pair_s

def find_closest_pair(points):
    """Main wrapper function."""
    if len(points) < 2:
        return 0, (None, None)
    # Presort points by X-coordinate once at the beginning
    points_sorted_x = sorted(points, key=lambda p: p[0])
    return closest_pair_recursive(points_sorted_x)

# --- Test Case ---
plane_points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
min_distance, closest_points = find_closest_pair(plane_points)

print(f"Closest distance: {min_distance:.4f}")
print(f"Between points: {closest_points[0]} and {closest_points[1]}")
# Output:
# Closest distance: 1.4142
# Between points: (2, 3) and (3, 4)
