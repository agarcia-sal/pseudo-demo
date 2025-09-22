# Start of the program

# Step 2: Receive Input
size = int(input())  # Read an integer from user input for the number of positions

# Step 3: Initialize List
positions = [True] * size  # Create a list with `size` elements, all initialized to True

# Step 4: Set Counters
current_increment = 1  # Initialize the increment counter
current_position_index = 0  # Initialize the position index

# Step 5: Mark Positions
while current_increment <= 500000:  # Continue incrementing until we reach 500,000
    # Check if the current position is still marked as True
    if positions[current_position_index]:  
        positions[current_position_index] = False  # Mark the position as False
    
    current_increment += 1  # Increment the counter
    
    # Update the position index with the current increment value, ensuring we wrap within the bounds of the list
    current_position_index = (current_position_index + current_increment) % size

# Step 6: Check Status of Positions
unmarked_positions = [pos for pos in positions if pos]  # Create a list of unmarked (True) positions

# Step 7: Output Result
if len(unmarked_positions) == 0:  # Check if there are any unmarked positions
    print("YES")  # All positions have been marked as False
else:
    print("NO")  # Some positions are still True

# End of the program
