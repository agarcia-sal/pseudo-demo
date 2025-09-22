# Initialize variables
number_of_positions = int(input())  # Get the number of positions from user input
marked_positions = [True] * number_of_positions  # Create a list of marked positions, all initially True
current_index = 0  # Starting index
step_count = 1  # Initialize step count

# Perform marking process
while step_count <= 500000:  # Loop until the step count exceeds 500,000
    if marked_positions[current_index]:  # Check if the current position is marked
        marked_positions[current_index] = False  # Mark this position as False
    
    step_count += 1  # Increment the step count
    current_index = (current_index + step_count) % number_of_positions  # Update current index with wrapping

# Check for unmarked positions
unmarked_positions = [position for position in marked_positions if position]  # Get all unmarked positions

# Output result
if not unmarked_positions:  # If there are no True values left in marked_positions
    print("YES")  # All positions are marked
else:
    print("NO")  # There are still unmarked positions
