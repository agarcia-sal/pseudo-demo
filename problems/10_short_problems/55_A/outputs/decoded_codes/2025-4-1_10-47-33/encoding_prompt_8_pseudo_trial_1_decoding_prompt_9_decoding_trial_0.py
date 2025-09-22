# Start Program

# Step 2: Get Input
n = int(input())  # Read an integer value from the user

# Step 3: Initialize List
IsMarked = [True] * n  # Create a list of size n with all elements set to True

# Step 4: Initialize Counters
currentIndex = 0  # Keeps track of the current index
increment = 1     # Step size for marking

# Step 5: Marking Process
while increment <= 500000:
    if IsMarked[currentIndex]:  # Check if the current item is still marked as True
        IsMarked[currentIndex] = False  # Mark this item as processed (set to False)
    
    increment += 1  # Increase the step for the next operation
    currentIndex = (currentIndex + increment) % n  # Wrap around if index exceeds list size

# Step 6: Check for Unmarked Items
UnmarkedItems = [item for item in IsMarked if item]  # Create a list of unmarked items (True entries)

# Step 7: Output Result
if len(UnmarkedItems) == 0:  # Check if there are any unmarked items
    print('YES')  # All items are marked
else:
    print('NO')   # There are unmarked items

# End Program
