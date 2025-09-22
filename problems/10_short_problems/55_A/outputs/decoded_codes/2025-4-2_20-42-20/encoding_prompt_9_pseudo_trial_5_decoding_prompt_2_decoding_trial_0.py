# Start

# Receive Input
size = int(input())

# Initialize List
positions = [True] * size  # Create a list of 'size' elements set to True

# Set Counters
current_increment = 1
current_position_index = 0

# Mark Positions
while current_increment <= 500000:
    if positions[current_position_index]:  # Check if the current position is True
        positions[current_position_index] = False  # Mark the position as False
    current_increment += 1  # Increment the current_increment by 1
    current_position_index = (current_position_index + current_increment) % size  # Update current_position_index using modulo

# Check Status of Positions
unmarked_positions = [pos for pos in positions if pos]  # Create a list of unmarked (True) positions

# Output Result
if len(unmarked_positions) == 0:
    print("YES")  # Output YES if all positions are marked
else:
    print("NO")   # Output NO if there are still unmarked positions

# End
