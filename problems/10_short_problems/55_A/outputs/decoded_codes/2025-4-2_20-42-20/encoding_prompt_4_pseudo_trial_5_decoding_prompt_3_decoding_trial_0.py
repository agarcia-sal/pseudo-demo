def main():
    # Step 1: Get user input as an integer
    n = int(input())
    
    # Step 2: Initialize a list of boolean values set to True for the range 0 to n
    isActive = [True] * n
    
    # Step 3: Initialize indices
    j = 0  # Current index initialization
    i = 1  # Step increment initialization

    # Step 4: Loop until i exceeds 500,000
    while i <= 500000:
        # Step 5: If the current position is active
        if isActive[j]:
            # Deactivate current position
            isActive[j] = False
        
        # Step 6: Increment step by 1
        i += 1
        
        # Step 7: Update index j in a circular manner
        j = (j + i) % n
    
    # Step 8: Create a list of active positions
    active_positions = [index for index, active in enumerate(isActive) if active]

    # Step 9: Check if there are any active positions
    if not active_positions:
        # If no active positions remain
        print('YES')
    else:
        # If there are still active positions
        print('NO')

# Execute the main function
if __name__ == "__main__":
    main()
