# Start of the code

# Step 1: Read an integer n from user input
n = int(input())

# Step 2: Initialize a list of size n with all elements set to True
is_not_deleted = [True] * n

# Step 3: Set initial variables
current_index = 0
i = 1

# Step 4: Loop through a range while i is less than or equal to 500000
while i <= 500000:
    # Check if the current index is marked as True
    if is_not_deleted[current_index]:
        # Mark the current index as False (deleted)
        is_not_deleted[current_index] = False
    
    # Increment i by 1
    i += 1
    
    # Update current_index to be (current_index + i) modulo n
    current_index = (current_index + i) % n

# Step 5: Create a new list containing all True elements from is_not_deleted
remaining_true = [value for value in is_not_deleted if value]

# Step 6: Determine output based on remaining values
if len(remaining_true) == 0:
    print('YES')  # If no True values remain
else:
    print('NO')   # If there are still True values

# End of the code
