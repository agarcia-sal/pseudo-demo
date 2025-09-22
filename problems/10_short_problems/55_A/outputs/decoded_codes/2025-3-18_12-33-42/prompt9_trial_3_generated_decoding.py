# Receive Input
n = int(input())  # Get the size of the list from user input

# Initialize Variables
is_active = [True] * n  # Create a list filled with True values
current_index = 0  # Track the current position in the list
step_count = 1  # Initial step size

# Perform Operations
while step_count <= 500000:
    if is_active[current_index]:  # Check if the current position is active
        is_active[current_index] = False  # Mark the position as inactive

    step_count += 1  # Increment the step count
    current_index = (current_index + step_count) % n  # Update the current index, wrapping around if needed

# Check Active Elements
active_elements = [i for i in is_active if i]  # List of active elements that are still True

# Determine Output
if not active_elements:  # If there are no active elements left
    print("YES")
else:
    print("NO")
