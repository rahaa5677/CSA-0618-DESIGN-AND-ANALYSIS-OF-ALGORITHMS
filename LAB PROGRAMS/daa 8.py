def tower_of_hanoi(n, source_rod, destination_rod, helper_rod):
    # Base Case: If there's only 1 disk left, move it directly
    if n == 1:
        print(f"Move disk 1 from {source_rod} to {destination_rod}")
        return

    # Step 1: Move top n-1 disks from Source to Helper
    tower_of_hanoi(n - 1, source_rod, helper_rod, destination_rod)

    # Step 2: Move the remaining largest disk from Source to Destination
    print(f"Move disk {n} from {source_rod} to {destination_rod}")

    # Step 3: Move the n-1 disks from Helper to Destination
    tower_of_hanoi(n - 1, helper_rod, destination_rod, source_rod)


# --- Execution Example ---
# Let's run the puzzle with 3 disks
number_of_disks = 3

print(f"Steps to solve Tower of Hanoi with {number_of_disks} disks:\n")
tower_of_hanoi(number_of_disks, source_rod='A', destination_rod='C', helper_rod='B')
