def main():
    # Step 1: Get input
    n = int(input())
    
    # Step 2: Initialize a boolean list of size n with all positions set to True
    positions = [True] * n

    # Step 3: Initialize index variables
    current_index = 0
    step = 1

    # Step 4: Loop through positions while step is less than or equal to 500,000
    while step <= 500000:
        # Check if the current position is still marked as True
        if positions[current_index]:
            # Mark the current position as False
            positions[current_index] = False
        
        # Increment step and update current_index
        step += 1
        current_index = (current_index + step) % n  # Wrap around using modulo n

    # Step 5: Check for unmarked positions
    unmarked_positions = [pos for pos in positions if pos]
    
    # Step 6: Output the result
    if len(unmarked_positions) == 0:
        print('YES')
    else:
        print('NO')

# To execute the main function
if __name__ == "__main__":
    main()
