# Step 1: Read the number of elements
number_of_elements = int(input())

# Step 2: Initialize the list with all elements set to True
marked_positions = [True] * number_of_elements

# Step 3: Initialize counters
current_index = 0  # Represents the current position being processed
step_size = 1      # The increment for marking positions

# Step 4: Iterative marking process
while step_size <= 500000:
    # If the current position is still marked as True
    if marked_positions[current_index]:
        # Mark the current position as False
        marked_positions[current_index] = False
    
    # Increment the step size for the next iteration
    step_size += 1
    
    # Calculate the next position to check
    current_index = (current_index + step_size) % number_of_elements

# Step 5: Check for remaining True values
remaining_true = [position for position in marked_positions if position]

# Step 6: Output result based on the remaining True values
if len(remaining_true) == 0:
    print("YES")  # All positions have been marked as False
else:
    print("NO")   # Some positions remain True
