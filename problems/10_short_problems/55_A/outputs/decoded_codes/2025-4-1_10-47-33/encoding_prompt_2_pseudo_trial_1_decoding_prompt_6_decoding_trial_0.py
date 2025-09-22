# Step 1: Read an integer value from the user
number_of_elements = int(input())

# Step 2: Create a Boolean list initialized to True
is_active = [True] * number_of_elements

# Step 3: Initialize indices
current_index = 0  # Current position in the is_active list
step_size = 1      # Step size for the elimination process

# Step 4: Start the elimination process
while step_size <= 500000:
    if is_active[current_index]:  # Check if the current position is still active
        is_active[current_index] = False  # Eliminate this position
    step_size += 1  # Increment the step size
    current_index = (current_index + step_size) % number_of_elements  # Update the current index

# Step 5: Check remaining active entries
remaining_active = [active for active in is_active if active]  # List of active positions

# Step 6: Determine and print the final result
if len(remaining_active) == 0:
    print("YES")  # All positions eliminated
else:
    print("NO")   # Some positions are still active
