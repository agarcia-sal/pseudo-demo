# Step 1: Initialize Variables
number_of_positions = int(input())  # Get an integer value for number of positions
marked_positions = [True] * number_of_positions  # Create a list with True values
current_index = 0  # Initialize current index
step_count = 1  # Initialize step count

# Step 2: Perform Marking Process
while step_count <= 500000:  # Loop until step count exceeds 500,000
    if marked_positions[current_index]:  # Check if the current position is marked
        marked_positions[current_index] = False  # Mark the position as False
    step_count += 1  # Increment the step count
    current_index = (current_index + step_count) % number_of_positions  # Update the current index

# Step 3: Check for Unmarked Positions
unmarked_positions = [pos for pos in marked_positions if pos]  # Get unmarked positions

# Output result
if not unmarked_positions:  # Check if the unmarked positions list is empty
    print("YES")  # All positions were marked
else:
    print("NO")  # There are still unmarked positions
