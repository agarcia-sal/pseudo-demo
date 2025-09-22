# Step 1: Input the total number of positions
total_positions = int(input())

# Step 2: Initialize a list to track marked positions
marked_positions = [True] * total_positions  # All positions start as unmarked (True)

# Step 3: Set initial index values
current_index = 0  # Tracking the current position in the list
step = 1  # Defines the increment in indices

# Step 4: Mark positions in a loop
while step <= 500000:  # Continue while step is less than or equal to 500,000
    if marked_positions[current_index]:  # If current position is unmarked
        marked_positions[current_index] = False  # Mark it as False (marked)

    step += 1  # Increment the step
    current_index = (current_index + step) % total_positions  # Update index with wrap-around

# Step 5: Check for unmarked positions
unmarked_positions = [pos for pos in marked_positions if pos]  # Identify unmarked positions

# Step 6: Output results
if not unmarked_positions:  # If there are no unmarked positions
    print("YES")  # All positions are marked
else:
    print("NO")  # There are unmarked positions
