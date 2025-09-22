# Start of the code

# Input: Read an integer value n, which represents the size of an array (or list)
n = int(input())

# Initialize: Create a list called is_available with n elements, all set to True
is_available = [True] * n

# Initialize the index and increment step
current_position = 0
increment = 1

# Processing Loop: While increment is less than or equal to 500,000
while increment <= 500000:
    # Check if is_available at current_position is True
    if is_available[current_position]:
        # If yes, mark it as unavailable
        is_available[current_position] = False
    
    # Increase increment for the next step
    increment += 1
    
    # Update current_position and wrap around using modulus
    current_position = (current_position + increment) % n

# Identify Unavailable Positions: Create available_positions list
available_positions = [i for i in is_available if i]

# Output: Check if there are any available positions
if len(available_positions) == 0:
    print("YES")
else:
    print("NO")

# End of the code
