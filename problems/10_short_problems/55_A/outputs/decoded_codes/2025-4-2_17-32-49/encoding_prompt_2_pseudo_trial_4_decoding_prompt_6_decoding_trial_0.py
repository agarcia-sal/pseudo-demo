# Start the program

# Step 2: Input
number_of_elements = int(input())  # Read an integer value n

# Step 3: Initialize
is_available = [True] * number_of_elements  # Create a list of n elements set to True
position = 0  # Initialize position index
step = 1  # Initialize steps

# Step 4: Loop until step exceeds 500,000
while step <= 500000:
    if is_available[position]:  # Check if the current position is available
        is_available[position] = False  # Mark this position as unavailable

    step += 1  # Increment step by 1
    position = (position + step) % number_of_elements  # Update the position, wrapping around the list

# Step 5: Check for available positions
available_positions = [idx for idx, available in enumerate(is_available) if available]  # Store available positions

# Step 6: Output Result
if len(available_positions) == 0:  # If no elements are available
    print("YES")  # All positions are unavailable
else:
    print("NO")  # Some positions are still available

# End
