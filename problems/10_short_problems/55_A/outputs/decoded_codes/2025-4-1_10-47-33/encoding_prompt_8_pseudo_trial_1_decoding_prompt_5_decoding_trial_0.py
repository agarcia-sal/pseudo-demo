# Start program

# Get input
n = int(input())  # Read an integer value representing the size of the list.

# Initialize list
IsMarked = [True] * n  # Create a list of size n, with all elements initially set to True.

# Initialize counters
current_index = 0  # This keeps track of which index in the list is being operated on.
increment = 1  # This is the step size for marking the list.

# Marking process
while increment <= 500000:
    if IsMarked[current_index]:  # Check if the current item is still marked as True.
        IsMarked[current_index] = False  # Mark this item as processed (set to False).
    
    increment += 1  # Increase the step for the next operation.
    current_index = (current_index + increment) % n  # Wrap around if the index exceeds the list size.

# Check for unmarked items
UnmarkedItems = [item for item in IsMarked if item]  # Create a list of unmarked items (still True).

# Output result
if len(UnmarkedItems) == 0:  # If there are no unmarked items (all are marked).
    print('YES')
else:
    print('NO')  # If there are still unmarked items, print 'NO'.

# End program
