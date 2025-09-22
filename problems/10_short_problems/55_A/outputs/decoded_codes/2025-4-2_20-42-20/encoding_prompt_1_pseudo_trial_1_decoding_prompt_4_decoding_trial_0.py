def main():
    # Step 1: Initialize the Program
    n = int(input())
    
    # Step 2: Create a boolean list
    isActive = [True] * n
    
    # Step 3: Set initial positions
    index = 0
    step = 1

    # Step 4: Iterate through steps
    while step <= 500000:
        # Check if the current position is active
        if isActive[index]:
            isActive[index] = False  # Deactivate the position
        
        step += 1  # Increment the step
        index = (index + step) % n  # Update index with wrap-around

    # Step 5: Check remaining active positions
    activePositions = [pos for pos in isActive if pos]

    # Step 6: Determine the output
    if len(activePositions) == 0:
        print("YES")  # All positions have been deactivated
    else:
        print("NO")   # There are still active positions

# Start the program
main()
