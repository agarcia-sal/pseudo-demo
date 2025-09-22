def mark_unavailable_positions():
    # Step 2: Input
    n = int(input())  # Read an integer value n
    
    # Step 3: Initialize
    isAvailable = [True] * n  # Create a list of n elements, all set to True
    position = 0  # This will track the current index in the list
    step = 1  # This represents the incrementing steps

    # Step 4: Loop until step exceeds 500,000
    while step <= 500000:
        if isAvailable[position]:  # Check if the current position is available
            isAvailable[position] = False  # Mark this position as unavailable
        step += 1  # Increment step by 1
        position = (position + step) % n  # Update position with wrapping

    # Step 5: Check for available positions
    availablePositions = [pos for pos in isAvailable if pos]  # List of available positions

    # Step 6: Output Result
    if len(availablePositions) == 0:  # If no available positions
        print("YES")  # Indicating all positions are marked unavailable
    else:  # Some positions are still available
        print("NO")

# Call the function to execute
mark_unavailable_positions()
