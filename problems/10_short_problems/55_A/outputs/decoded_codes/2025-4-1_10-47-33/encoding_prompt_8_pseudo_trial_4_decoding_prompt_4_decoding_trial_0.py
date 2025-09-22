# This program checks if there are any True values left in a list after a series of operations

# Step 1: Read Input
total_numbers = int(input())

# Step 2: Initialize List
status_list = [True] * total_numbers

# Step 3: Set Initial Indices
current_index = 0
step = 1

# Step 4: Loop Until Limit Reached
while step <= 500000:
    # Check if the current index is True
    if status_list[current_index]:
        # Mark current index as False
        status_list[current_index] = False

    # Step forward
    step += 1
    
    # Update current index with circular wrapping
    current_index = (current_index + step) % total_numbers

# Step 5: Check Remaining True Values
remaining_true_values = [value for value in status_list if value]

# Step 6: Output Result
if len(remaining_true_values) == 0:
    print("YES")
else:
    print("NO")
