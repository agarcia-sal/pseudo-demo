# Start of the program

# Step 2: Receive Input
size = int(input())  # Read an integer to determine the number of positions

# Step 3: Initialize List
positions = [True] * size  # Create a list of size 'size' initialized to True

# Step 4: Set Counters
current_increment = 1  # Initialize the increment counter
current_position_index = 0  # Initialize the position index

# Step 5: Mark Positions
while current_increment <= 500000:  # Limit the increments to 500,000
    if positions[current_position_index]:  # Check if the current position is marked as True
        positions[current_position_index] = False  # Mark the position as False
        
    current_increment += 1  # Increment the current_increment by 1
    current_position_index += current_increment  # Update the current position index
    current_position_index %= size  # Wrap the index around using modulo operation

# Step 6: Check Status of Positions
unmarked_positions = [pos for pos in positions if pos]  # List of positions still marked True

# Step 7: Output Result
if len(unmarked_positions) == 0:  # If no unmarked positions are left
    print("YES")  # Output YES
else:
    print("NO")   # Output NO

# End of the program
