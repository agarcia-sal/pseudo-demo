# Step 1: Start

# Step 2: Receive Input
size = int(input())  # Read an integer called size from the user

# Step 3: Initialize List
positions = [True] * size  # Create a list called positions containing size elements all set to True

# Step 4: Set Counters
current_increment = 1  # Initialize current_increment to 1
current_position_index = 0  # Initialize current_position_index to 0

# Step 5: Mark Positions
while current_increment <= 500000:
    if positions[current_position_index]:  # If positions[current_position_index] is True
        positions[current_position_index] = False  # Set positions[current_position_index] to False
    current_increment += 1  # Increment current_increment by 1
    current_position_index = (current_position_index + current_increment) % size  # Update current_position_index using modulo operation

# Step 6: Check Status of Positions
unmarked_positions = [pos for pos in positions if pos]  # Create a new list containing only the True values from positions

# Step 7: Output Result
if len(unmarked_positions) == 0:  # If the length of unmarked_positions is 0
    print("YES")  # Print YES
else:
    print("NO")  # Otherwise, print NO

# Step 8: End
