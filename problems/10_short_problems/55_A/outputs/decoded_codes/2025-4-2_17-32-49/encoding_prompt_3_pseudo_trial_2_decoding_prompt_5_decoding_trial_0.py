# Step 1: Obtain the input value for n
number_of_elements = int(input())

# Step 2: Initialize a boolean list to track the current state of numbers
is_active_list = [True] * number_of_elements

# Step 3: Initialize counters for iteration
current_index = 0
step = 1

# Step 4: Loop until the step count exceeds 500,000
while step <= 500000:
    # Step 5: Check if the current position in the list is active
    if is_active_list[current_index]:
        # Mark the current position as inactive
        is_active_list[current_index] = False

    # Step 6: Move to the next step
    step += 1
    # Update the current index using the formula modulus n
    current_index = (current_index + step) % number_of_elements

# Step 7: Create a new list containing only the active elements
active_elements = [element for element in is_active_list if element]

# Step 8: Check if there are any active elements remaining
if len(active_elements) == 0:
    print('YES')  # All elements are inactive
else:
    print('NO')   # There are still active elements
