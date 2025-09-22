# Start the program

# Step 1: Get an integer input for max_index
max_index = int(input())

# Step 2: Create a list called boolean_list initialized with True values of size max_index
boolean_list = [True] * max_index

# Step 3: Initialize variables for current_index and current_step
current_index = 0
current_step = 1

# Step 4: Process up to 500,000 steps
while current_step <= 500000:
    # If the current index is marked True, mark it as False
    if boolean_list[current_index]:
        boolean_list[current_index] = False  # Mark this index as processed
    
    # Increment the step
    current_step += 1
    
    # Update the current index using modulo to wrap around
    current_index = (current_index + current_step) % max_index

# Step 5: Create a new list for any remaining True values
remaining_true_indices = [value for value in boolean_list if value]

# Step 6: Check if there are any True values left
if len(remaining_true_indices) == 0:
    # Output 'YES' if all indices have been marked
    print('YES')
else:
    # Output 'NO' if there are still unmarked indices
    print('NO')

# End the program
