# Start

# Receive Input
size = int(input())  # Read the size of the list from the user

# Initialize List
positions = [True] * size  # Create a list with 'size' elements set to True

# Set Counters
current_increment = 1
current_position_index = 0

# Mark Positions
while current_increment <= 500000:
    if positions[current_position_index]:  # If the position is marked as True
        positions[current_position_index] = False  # Mark it as False
    
    current_increment += 1  # Increment the counter
    # Update the position index with wrap-around using modulo
    current_position_index = (current_position_index + current_increment) % size

# Check Status of Positions
unmarked_positions = [pos for pos in positions if pos]  # Create a list of unmarked (True) positions

# Output Result
if len(unmarked_positions) == 0:  # If no unmarked (True) positions are left
    print("YES")
else:
    print("NO")

# End
