def main():
    # Step 1: Input
    n = int(input())
    
    # Step 2: Initialization
    is_present = [True] * n  # List to track available positions
    index = 0                # Current position in the list
    step = 1                 # Number of positions to move forward after each iteration

    # Step 3: Processing Loop
    while step <= 500000:
        if is_present[index]:
            is_present[index] = False  # Mark the position as not available
        
        step += 1                      # Increment the step
        index = (index + step) % n     # Calculate the next position, wrapping around if needed

    # Step 4: Checking Results
    available_positions = [pos for pos in is_present if pos]  # List of positions that are still True
    
    if len(available_positions) == 0:
        print("YES")  # All positions are marked as not available
    else:
        print("NO")   # Some positions are still available

if __name__ == "__main__":
    main()
