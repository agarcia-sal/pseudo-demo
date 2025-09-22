# Start the program

# Step 1: Get input from the user
n = int(input())  # Read the integer value which represents the number of positions

# Step 2: Initialize the list of positions
positions = [True] * n  # Create a list initialized to True for all n positions

# Step 3: Set initial counter variables
count = 1  # This will be our step increment
current_index = 0  # This will point to the current position in the list

# Step 4: Mark positions in a loop
while count <= 500000:  # Repeat while count is less than or equal to 500,000
    if positions[current_index]:  # Check if the current position is still marked as unmarked
        positions[current_index] = False  # Mark the position as False (marked)
    
    count += 1  # Increment count by 1
    current_index = (current_index + count) % n  # Update current_index and wrap around using modulo

# Step 5: Check for unmarked positions
unmarked_positions = [pos for pos in positions if pos]  # Create a list of unmarked positions

# Step 6: Produce output
if len(unmarked_positions) == 0:  # If there are no unmarked positions
    print("YES")  # All positions have been marked
else:
    print("NO")  # There are still unmarked positions

# End the program
