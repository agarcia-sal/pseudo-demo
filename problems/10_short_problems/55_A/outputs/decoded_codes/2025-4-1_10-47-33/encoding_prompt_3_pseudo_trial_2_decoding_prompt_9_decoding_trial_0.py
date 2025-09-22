# Start of the program

# Step 1: Get the input for the number of elements
number_of_elements = int(input())

# Step 2: Create a list initialized with True values
is_active = [True] * number_of_elements

# Step 3: Initialize index and step variables
index = 0
step = 1

# Step 4: Loop as long as step is less than or equal to 500000
while step <= 500000:
    # Step 4a: Check if the current index is True
    if is_active[index]:
        # Step 4i: Mark the index as inactive
        is_active[index] = False
    
    # Step 4b: Increment step by 1
    step += 1
    
    # Step 4c: Update index using modulo to wrap around
    index = (index + step) % number_of_elements

# Step 5: Create a list of active elements still marked as True
active_elements = [element for element in is_active if element]

# Step 6: Check if there are any remaining active elements
if len(active_elements) == 0:
    print('YES')  # No active elements remaining
else:
    print('NO')   # There are active elements remaining

# End of the program
