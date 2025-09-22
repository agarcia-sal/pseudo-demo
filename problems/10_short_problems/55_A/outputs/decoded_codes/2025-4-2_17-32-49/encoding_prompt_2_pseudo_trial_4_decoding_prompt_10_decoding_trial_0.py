def main():
    # Step 2: Input the number of elements
    n = int(input())
    
    # Step 3: Initialize the variables
    is_available = [True] * n  # All elements initialized to True
    position = 0
    step = 1
    
    # Step 4: Loop until the step exceeds 500,000
    while step <= 500000:
        if is_available[position]:  # If the position is available
            is_available[position] = False  # Mark it as unavailable
        step += 1  # Increment the step
        position = (position + step) % n  # Update the position with wrap-around
    
    # Step 5: Check for available positions
    available_positions = [index for index, available in enumerate(is_available) if available]
    
    # Step 6: Output the result
    if not available_positions:  # If no positions are available
        print("YES")  # All positions are marked unavailable
    else:
        print("NO")  # Some positions are still available

# Call the main function to execute the code
if __name__ == "__main__":
    main()
