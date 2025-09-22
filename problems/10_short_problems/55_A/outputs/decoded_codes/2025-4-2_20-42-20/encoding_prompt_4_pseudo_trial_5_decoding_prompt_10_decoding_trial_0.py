def main():
    # Step 1: Get user input as an integer n
    n = int(input())
    
    # Step 2: Initialize a list of boolean values to True for the range 0 to n
    is_active = [True] * n

    # Step 3: Initialize indices
    j = 0  # Current index in the boolean list
    i = 1  # Step increment starting from 1

    # Step 4: Loop until i exceeds 500,000
    while i <= 500000:
        # If the current position is active
        if is_active[j]:
            # Deactivate current position
            is_active[j] = False
        
        # Increment step by 1
        i += 1
        
        # Update index j in a circular manner
        j = (j + i) % n

    # Step 5: Create a list of active positions
    active_positions = [index for index, value in enumerate(is_active) if value]

    # Step 6: Check if there are any active positions
    if len(active_positions) == 0:
        print('YES')  # No active positions remain
    else:
        print('NO')   # There are still active positions

# Entry point of the program
if __name__ == "__main__":
    main()
