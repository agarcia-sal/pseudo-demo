# Start of the program

# Step 2: Read an integer value n, which represents the size of the list.
n = int(input())

# Step 3: Initialize the list and variables
# Create a list called is_available with n elements, all set to True
is_available = [True] * n  # This list tracks the availability of each position
current_position = 0  # This variable serves as the index to access the list
increment = 1  # Represents the current step size

# Step 4: Processing Loop
while increment <= 500000:
    # Check if is_available at current_position is True
    if is_available[current_position]:
        # If yes, set is_available at that index to False
        is_available[current_position] = False
    
    # Increase the increment by 1 for the next step
    increment += 1
    
    # Update current_position and wrap around using modulus if necessary
    current_position = (current_position + increment) % n

# Step 5: Identify Unavailable Positions
available_positions = [pos for pos in is_available if pos]  # Collect all True values

# Step 6: Output the result based on availability
if len(available_positions) == 0:  # If no positions are available
    print("YES")
else:  # If there are available positions
    print("NO")

# End of the program
