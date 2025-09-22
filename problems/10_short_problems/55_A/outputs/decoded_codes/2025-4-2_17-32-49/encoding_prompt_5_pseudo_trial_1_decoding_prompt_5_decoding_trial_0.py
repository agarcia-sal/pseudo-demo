# Start the program

# Get Input
n = int(input())  # Read the number of positions from the user

# Initialize List of Positions
positions = [True] * n  # Create a list with all entries set to True (unmarked)

# Set Initial Counter Variables
count = 1  # Step increment
current_index = 0  # Current position in the list

# Mark Positions in a Loop
# Repeat while count is less than or equal to 500,000
while count <= 500000:
    if positions[current_index]:  # If the position is still marked as True
        positions[current_index] = False  # Mark it as False (marked)
    
    count += 1  # Increment the count
    # Calculate new current_index using modulo for wrapping around
    current_index = (current_index + count) % n  

# Check for Unmarked Positions
unmarked_positions = [pos for pos in positions if pos]  # List of entries still marked as True

# Produce Output
if len(unmarked_positions) == 0:  # If all positions are marked
    print("YES")  # All positions have been marked
else:
    print("NO")  # There are still unmarked positions

# End the program
