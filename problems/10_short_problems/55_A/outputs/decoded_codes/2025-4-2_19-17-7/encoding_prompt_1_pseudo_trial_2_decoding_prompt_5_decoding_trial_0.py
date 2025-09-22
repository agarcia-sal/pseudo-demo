# Begin the process

# Step 2: Read an integer value n from the user
n = int(input())

# Step 3: Initialize variables
is_active = [True] * n  # Create a list of size n with all elements set to True
current_index = 0       # Initialize current index to 0
increment = 1           # Initialize increment to 1

# Step 4: Loop while incrementing increment up to 500,000
for increment in range(1, 500001):  # Loop from 1 to 500,000
    if is_active[current_index]:     # Check if current index is active
        is_active[current_index] = False  # Set the current index to False (deactivate it)

    # Update current index and wrap around using modulo n
    current_index = (current_index + increment) % n

# Step 5: Check for active elements
active_elements = [x for x in is_active if x]  # List of elements that are still True

# Step 6: Output result
if len(active_elements) == 0:  # If there are no active elements
    print('YES')                # Print 'YES'
else:
    print('NO')                 # Otherwise, print 'NO'

# End the process
