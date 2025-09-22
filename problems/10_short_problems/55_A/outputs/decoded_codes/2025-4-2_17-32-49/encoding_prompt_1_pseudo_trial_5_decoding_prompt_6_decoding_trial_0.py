# Start the program

# Input a number n (the maximum size of the list)
n = int(input())

# Create a list isAvailable of size n and set all elements to True
is_available = [True] * n

# Initialize two variables
current_position = 0  # This will track the index in isAvailable
increment_value = 1   # This will be the current step size

# Set a loop to run while incrementValue is less than or equal to 500,000
while increment_value <= 500000:
    # If the element at isAvailable[currentPosition] is True
    if is_available[current_position]:
        # Set isAvailable[currentPosition] to False (mark as unavailable)
        is_available[current_position] = False
    
    # Increment incrementValue by 1 (move to the next step)
    increment_value += 1
    
    # Update currentPosition to the new position calculated
    current_position = (current_position + increment_value) % n  # Wrap around if exceeds size of the list

# Create a new list availablePositions that includes all positions from isAvailable that are still True
available_positions = [i for i in is_available if i]

# Check the length of availablePositions
if len(available_positions) == 0:
    # Output "YES" (indicating all positions were made unavailable)
    print("YES")
else:
    # Output "NO" (indicating there are still available positions)
    print("NO")

# End the program
