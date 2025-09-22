# Start

# Input: Read an integer value n
n = int(input())

# Initialize: Create a list called is_available with n elements, all set to True
is_available = [True] * n  # A list of True values of size n
current_position = 0  # Set the index to 0
increment = 1  # Set current step size to 1

# Processing Loop: While increment is less than or equal to 500,000
while increment <= 500000:
    # Check if is_available at index current_position is True
    if is_available[current_position]:
        # If yes, set is_available at that index to False
        is_available[current_position] = False
    
    # Increase the increment by 1
    increment += 1
    # Update the current_position with wrap-around using modulus n
    current_position = (current_position + increment) % n

# Identify Unavailable Positions: Create a list of available_positions
available_positions = [pos for pos in is_available if pos]

# Output: Check if the length of available_positions is 0
if len(available_positions) == 0:
    print("YES")  # Print "YES" if no positions are available
else:
    print("NO")   # Print "NO" otherwise

# End
