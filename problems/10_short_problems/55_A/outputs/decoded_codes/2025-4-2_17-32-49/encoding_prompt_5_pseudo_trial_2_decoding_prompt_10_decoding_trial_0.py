def main():
    # Step 1: Initialize Variables
    n = int(input())  # Read the size of the list
    b = [True] * n    # Create a list initialized with True values
    j = 0             # Starting index
    i = 1             # Starting iteration count

    # Step 2: Process the List
    while i <= 500000:
        if b[j]:  # Check if current position is still True
            b[j] = False  # Mark this position as visited (False)
        i += 1  # Move to the next step
        j = (j + i) % n  # Update j using modulo to wrap around

    # Step 3: Determine Remaining Values
    remaining_true_values = [value for value in b if value]  # Filter out remaining True values
    
    # Step 4: Output the result
    if len(remaining_true_values) == 0:
        print("YES")  # All positions were marked as visited
    else:
        print("NO")   # Some positions remain unvisited

# Run the main function
main()
