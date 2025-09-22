def main():
    # Step 1: Input the number of elements
    n = int(input())
    
    # Step 2: Initialize the tracking list and other variables
    is_true = [True] * n  # List to track the status of each position
    current_index = 0      # Variable to track the current index
    step = 1               # Step to determine the update in current index

    # Step 3: Loop until step exceeds 500,000
    while step <= 500000:
        # Check if the position at current_index is True
        if is_true[current_index]:
            is_true[current_index] = False  # Set the current position to False
        
        # Increment the step counter
        step += 1
        
        # Update the current index using modular arithmetic
        current_index = (current_index + step) % n

    # Step 4: Filter remaining True values
    remaining_true = [value for value in is_true if value]

    # Step 5: Check outcome and print result
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Entry point for the program
if __name__ == "__main__":
    main()
