# Start the program

# Get Input
n = int(input())  # Read an integer value from the user for the number of positions

# Initialize List of Positions
positions = [True] * n  # Create a list with n entries, all set to True (unmarked)

# Set Initial Counter Variables
count = 1  # Initial step increment
current_index = 0  # Starting position in the list

# Mark Positions in a Loop
while count <= 500000:  # Loop until count exceeds 500,000
    if positions[current_index]:  # Check if the current position is unmarked
        positions[current_index] = False  # Mark the position as False (marked)
    
    count += 1  # Increment the step count
    current_index = (current_index + count) % n  # Update current index with wrap around

# Check for Unmarked Positions
unmarked_positions = [pos for pos in positions if pos]  # Create a list of all unmarked positions

# Produce Output
if len(unmarked_positions) == 0:  # If there are no unmarked positions
    print("YES")  # All positions have been marked
else:
    print("NO")  # There are still unmarked positions

# End the program
