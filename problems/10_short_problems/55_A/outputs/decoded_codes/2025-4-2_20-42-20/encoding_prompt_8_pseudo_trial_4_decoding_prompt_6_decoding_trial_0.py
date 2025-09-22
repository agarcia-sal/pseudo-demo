# Get input from the user for the size of the list
size_of_list = int(input())

# Initialize a boolean list to track unmarked positions
positions = [True] * size_of_list

# Index variables
current_index = 0  # This will track the current position being processed
step = 1           # Step determines how far to move in each iteration

# Loop through positions with a maximum step of 500,000
while step <= 500000:
    if positions[current_index]:  # Check if the current position is still True
        positions[current_index] = False  # Mark the position as False

    step += 1  # Increment the step
    current_index = (current_index + step) % size_of_list  # Update current index with wrap-around

# Create a list of unmarked positions
unmarked_positions = [pos for pos in positions if pos]

# Output the result
if len(unmarked_positions) == 0:
    print('YES')  # All positions have been marked
else:
    print('NO')   # There are still unmarked positions
