def main():
    # Step 1: Initialize Variables
    n = int(input())  # Read the size of the list
    b = [True] * n    # Create a list of size n, initialized with True
    j = 0             # Initialize index j
    i = 1             # Initialize index i

    # Step 2: Process the List
    while i <= 500000:
        if b[j]:  # Check if the current position is True
            b[j] = False  # Mark this position as visited
        i += 1  # Increment i for the next iteration
        j = (j + i) % n  # Update j using modulo n for wrapping around

    # Step 3: Determine Remaining Values
    x = [value for value in b if value]  # Create a list of remaining True values

    # Output result based on the presence of True values in list x
    if len(x) == 0:
        print("YES")  # All positions were marked as visited
    else:
        print("NO")   # Some positions remain unvisited

# Call the main function to execute the program
main()
