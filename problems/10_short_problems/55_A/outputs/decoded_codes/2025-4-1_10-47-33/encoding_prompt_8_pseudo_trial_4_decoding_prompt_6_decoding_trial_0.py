# Step 1: Read input for the total number of entries
total_numbers = int(input())

# Step 2: Initialize a list with all entries set to True
status_list = [True] * total_numbers

# Step 3: Set index for current position and initialize step
current_index = 0
step = 1

# Step 4: Loop until the step limit is reached
while step <= 500000:
    # Check if the current status is True
    if status_list[current_index]:
        # Mark it as False
        status_list[current_index] = False
    # Increase step
    step += 1
    # Update current_index in a circular manner
    current_index = (current_index + step) % total_numbers

# Step 5: Check for remaining True values
remaining_true_values = [value for value in status_list if value]

# Step 6: Output the result based on remaining True values
if len(remaining_true_values) == 0:
    print("YES")
else:
    print("NO")
