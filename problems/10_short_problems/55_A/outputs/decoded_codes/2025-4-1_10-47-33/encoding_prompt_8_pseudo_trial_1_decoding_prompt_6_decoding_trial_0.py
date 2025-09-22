# Start Program

# Step 2: Get Input
n = int(input())  # Read an integer value from the user

# Step 3: Initialize List
is_marked = [True] * n  # Create a list called 'is_marked' of size 'n' all initialized to True

# Step 4: Initialize Counters
current_index = 0  # Keeps track of which index is being operated on
increment = 1  # Step size for marking the list

# Step 5: Marking Process
while increment <= 500000:  # While increment is less than or equal to 500000
    if is_marked[current_index]:  # If the current item is still marked as True
        is_marked[current_index] = False  # Mark this item as processed
    increment += 1  # Increment the step for the next operation
    current_index = (current_index + increment) % n  # Update current index, wrapping around if necessary

# Step 6: Check for Unmarked Items
unmarked_items = [item for item in is_marked if item]  # Create a list of unmarked items (True values)

# Step 7: Output Result
if len(unmarked_items) == 0:  # If there are no unmarked items
    print('YES')
else:
    print('NO')  # Otherwise, print 'NO'

# End Program
