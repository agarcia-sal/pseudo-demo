# Input the total number of positions
total_positions = int(input())

# Initialize a list to track marked positions
marked_positions = [True] * total_positions  # All positions are initially marked

# Set initial index values
current_index = 0
step = 1

# Mark positions in a loop
while step <= 500000:
    if marked_positions[current_index]:  # Check if the position is unmarked
        marked_positions[current_index] = False  # Mark the position
    step += 1  # Increment the step
    current_index = (current_index + step) % total_positions  # Update to the next position

# Check for unmarked positions
unmarked_positions = [pos for pos in marked_positions if pos]  # Identify unmarked positions

# Output results
if not unmarked_positions:
    print("YES")  # All positions are marked
else:
    print("NO")  # There are unmarked positions
