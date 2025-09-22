# Begin Process

# Step 2: Input - Read an integer value from the user
number_of_elements = int(input())

# Step 3: Initialize - Create a list with all elements set to True
is_active = [True] * number_of_elements  # List of size n with all True values
current_index = 0                         # Index starts at 0
increment = 1                              # Starting increment value

# Step 4: Loop - Incrementing up to 500,000
for increment in range(1, 500001):        # Loop from 1 to 500,000 inclusive
    if is_active[current_index]:          # Check if current index is True
        is_active[current_index] = False  # Set it to False

    current_index = (current_index + increment) % number_of_elements  # Update index

# Step 5: Check for Active Elements
active_elements = [element for element in is_active if element]  # List of all active (True) elements

# Step 6: Output - Check if there are active elements
if len(active_elements) == 0:             # If there are no active elements
    print('YES')                           # Print 'YES'
else:
    print('NO')                            # Otherwise, print 'NO'

# End Process
