# Start

# Step 1: Input
n = int(input())  # Read an integer value n representing the size of the array

# Step 2: Initialize
is_available = [True] * n  # Create a list of size n with all values set to True
current_position = 0        # Set the current position index to 0
increment = 1               # Initialize increment to 1

# Step 3: Processing Loop
# Working through the increment until it reaches or exceeds 500,000
while increment <= 500000:
    # Check if the current position is available
    if is_available[current_position]:
        is_available[current_position] = False  # Mark the position as unavailable

    # Prepare for the next iteration
    increment += 1
    current_position = (current_position + increment) % n  # Update position and wrap around using modulus

# Step 4: Identify Unavailable Positions
available_positions = [index for index, available in enumerate(is_available) if available]  # Collect all available positions

# Step 5: Output
if len(available_positions) == 0:  # If there are no available positions, output "YES"
    print("YES")
else:  # Otherwise, output "NO"
    print("NO")

# End
