# Initialize the program by reading an integer value from user input.
num_positions = int(input())  # Read an integer value 'n'

# Create a boolean list with 'n' elements, all initialized to True.
is_active = [True] * num_positions

# Set initial positions for iteration
current_index = 0  # This will track the current position in the list
step_count = 1     # This will determine how many steps to move after each iteration

# Iterate through steps while step_count is less than or equal to 500,000
while step_count <= 500000:
    # Check if the current position in is_active is True
    if is_active[current_index]:
        is_active[current_index] = False  # Deactivate this position
    
    step_count += 1  # Increment step_count by 1
    current_index = (current_index + step_count) % num_positions  # Update index and wrap around

# Check remaining active positions
active_positions = [pos for pos in is_active if pos]  # List of still active positions

# Determine the output based on the active positions
if len(active_positions) == 0:  # If no True values are left
    print("YES")  # Indicating all positions have been deactivated
else:
    print("NO")   # Indicating that there are still active positions
