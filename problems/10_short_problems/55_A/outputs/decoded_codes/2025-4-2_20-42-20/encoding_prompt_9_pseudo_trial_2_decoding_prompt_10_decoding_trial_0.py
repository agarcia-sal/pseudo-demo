def main():
    # Step 1: Receive input for total positions
    total_positions = int(input())
    
    # Step 2: Initialize list with True values
    positions = [True] * total_positions
    
    # Step 3: Set initial indices
    current_index = 0
    step = 1
    
    # Step 4: Iterate through the marking process
    while step <= 500000:
        if positions[current_index]:  # If the position is unmarked
            positions[current_index] = False  # Mark the position as False
        
        step += 1  # Increment the step
        current_index = (current_index + step) % total_positions  # Calculate the next position
    
    # Step 5: Check for unmarked positions
    remaining_unmarked = [pos for pos in positions if pos]
    
    # Step 6: Determine result
    if not remaining_unmarked:  # If there are no unmarked positions
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
