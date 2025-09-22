def main():
    # Step 1: Receive input
    n = int(input())  # Read a number n which represents the size of the list

    # Step 2: Initialize boolean list
    boolean_list = [True] * n  # Create a list of size n initialized to True

    # Step 3: Set up iteration variables
    current_index = 0  # Initialize currentIndex to 0
    step = 1  # Initialize step to 1

    # Step 4: Mark elements process
    while step <= 500000:
        if boolean_list[current_index]:  # Check current position
            boolean_list[current_index] = False  # Mark this position as False (indicating it has been marked)
        step += 1  # Increment step value
        current_index = (current_index + step) % n  # Calculate next position with wrapping around

    # Step 5: Extract remaining unmarked elements
    remaining_true = [pos for pos in boolean_list if pos]  # List of unmarked (True) positions

    # Step 6: Check results
    if len(remaining_true) == 0:  # If no unmarked positions
        print("YES")  # All positions were marked
    else:
        print("NO")  # At least one position remained unmarked

# Execute the main function when the script is run
if __name__ == "__main__":
    main()
