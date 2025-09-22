# Start Program

# Step 2: Get Input
n = int(input())  # Read an integer value from the user

# Step 3: Initialize List
IsMarked = [True] * n  # Create a list of size n, initialized to True

# Step 4: Initialize Counters
currentIndex = 0  # Keeps track of the current index in the list
increment = 1  # Step size for marking

# Step 5: Marking Process
while increment <= 500000:  # Continue the marking process while increment is within the limit
    if IsMarked[currentIndex]:  # Check if the current item is marked as True (unmarked)
        IsMarked[currentIndex] = False  # Mark this item as processed (unmark it)

    increment += 1  # Increase the step for the next operation
    currentIndex = (currentIndex + increment) % n  # Update currentIndex using modulo to wrap around

# Step 6: Check for Unmarked Items
UnmarkedItems = [item for item in IsMarked if item]  # Create a list of all still marked (True) items

# Step 7: Output Result
if len(UnmarkedItems) == 0:  # If there are no unmarked items
    print('YES')
else:
    print('NO')  # If any items remain unmarked

# End Program
