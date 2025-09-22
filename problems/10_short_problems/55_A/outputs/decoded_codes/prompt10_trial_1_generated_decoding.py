def main():
    # Step 1: Initialize Variables
    n = int(input())  # Get user input for the size of the array
    b = [True] * n    # Create a list of boolean values initialized to True
    j = 0             # Initialize j to 0
    i = 1             # Initialize i to 1

    # Step 2: Loop Structure
    while i <= 500000:
        # Step 3: Conditional Logic
        if b[j]:
            b[j] = False  # Mark the index as not valid

        # Step 4: Increment Variables
        i += 1
        j = (j + i) % n  # Update index j using modulo to wrap around

    # Step 5: Filter Remaining Values
    x = [value for value in b if value]  # Create a list with elements from b that are still True

    # Step 6: Final Conditional Check
    if len(x) == 0:
        print("YES")  # If no True values remain, output "YES"
    else:
        print("NO")   # Otherwise, output "NO"

# Run the main function
if __name__ == "__main__":
    main()
