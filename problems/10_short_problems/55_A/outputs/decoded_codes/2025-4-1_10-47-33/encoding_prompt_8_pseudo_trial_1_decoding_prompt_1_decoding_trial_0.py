# Start Program

# Get Input:
n = int(input())  # Read an integer value n from the user, which represents the size of a list.

# Initialize List:
IsMarked = [True] * n  # Create a list called IsMarked of size n with all elements set to True.

# Initialize Counters:
currentIndex = 0  # Set currentIndex to 0.
increment = 1  # Set increment to 1.

# Marking Process:
while increment <= 500000:  # While increment is less than or equal to 500000:
    if IsMarked[currentIndex]:  # If the current item in IsMarked at currentIndex is True:
        IsMarked[currentIndex] = False  # Mark this item as processed by changing it to False.
    increment += 1  # Increment step for the next operation.
    currentIndex = (currentIndex + increment) % n  # Update currentIndex.

# Check for Unmarked Items:
UnmarkedItems = [item for item in IsMarked if item]  # Create a list of all unmarked items (those that are still True).

# Output Result:
if len(UnmarkedItems) == 0:  # If the length of UnmarkedItems is 0:
    print('YES')  # All items are marked.
else:
    print('NO')  # Some items are unmarked.

# End Program
