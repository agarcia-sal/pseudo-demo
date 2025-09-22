def main():
    # Step 2: Get Input
    n = int(input())
    
    # Step 3: Initialize List
    marked = [True] * n
    
    # Step 4: Set Initial Variables
    current_index = 0
    step = 1
    
    # Step 5: Mark Unmarked Positions
    while step <= 500000:
        if marked[current_index]:  # Check if the current position is unmarked
            marked[current_index] = False  # Mark this position
            
        step += 1  # Increase the step size
        current_index = (current_index + step) % n  # Calculate new position (circular)
    
    # Step 6: Check for Unmarked Positions
    unmarked_positions = [mark for mark in marked if mark]  # Gather all unmarked positions
    
    # Step 7: Determine Output
    if not unmarked_positions:  # If no unmarked positions left
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
if __name__ == "__main__":
    main()
