def main():
    # Step 2: Receive Input
    size = int(input())
    
    # Step 3: Initialize List
    positions = [True] * size  # Create a list of True values
    
    # Step 4: Set Counters
    current_increment = 1
    current_position_index = 0
    
    # Step 5: Mark Positions
    while current_increment <= 500000:
        if positions[current_position_index]:  # If position is unmarked
            positions[current_position_index] = False  # Mark it as false
        
        current_increment += 1  # Increment the current increment
        # Update the current position index and wrap it within the bounds of the list
        current_position_index = (current_position_index + current_increment) % size
    
    # Step 6: Check Status of Positions
    unmarked_positions = [pos for pos in positions if pos]  # Gather all unmarked positions (True values)
    
    # Step 7: Output Result
    if len(unmarked_positions) == 0:
        print("YES")
    else:
        print("NO")

# Step 1: Start the program
if __name__ == "__main__":
    main()
